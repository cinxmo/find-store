#!/usr/bin/env python

"""
Find Store
  find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>            Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address="<address>"  Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)        Display units in miles or kilometers [default: mi]
  --output=(text|json)   Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example
  find_store --address="1770 Union St, San Francisco, CA 94123"
  find_store --zip=94115 --units=km
"""

from math import cos, asin, sqrt

import geocoder
import pandas as pd

from docopt import docopt
from .util import valid_zip, convert_mi_to_km


def get_distance(lat1, lon1, lat2, lon2):
    """
    Haversine formula
    :param lat1: latitude of 1st location
    :param lon1: longitude of 1st location
    :param lat2: latitude of 2nd location
    :param lon2: longitude of 2nd location
    :return: distance in km
    """
    r = 3958.8  # radius of earth in miles
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 2 * r * asin(sqrt(a))


def get_closest_stores(lat, long):
    """
    :param lat: latitude
    :param long: longitude
    :return: all row(s) where the distance is equal to the minimum distance from the input latitude and longitude
    """
    store_locations = pd.read_csv("find_store/data/store-locations.csv")
    store_locations["Distance"] = store_locations.apply(lambda p:
        get_distance(p["Latitude"], p["Longitude"], lat, long),
        axis=1
    )
    min_distance_row = store_locations[store_locations["Distance"] == store_locations["Distance"].min()]
    return min_distance_row


def main():
    arguments = docopt(__doc__)

    address = arguments["--address"]
    zip = arguments["--zip"]
    units = arguments["--units"]
    output = arguments["--output"]

    # verify zip
    if zip:
        if not valid_zip(zip):
            print(f"Please verify that your zip code input is valid. You've inputted {zip}")
            return

    # convert to latitude, longitude
    location = zip if zip else address
    location = geocoder.google(location)
    latitude, longitude = location.latlng

    # find closest store
    closest_stores = get_closest_stores(latitude, longitude)
    # get first row if multiple rows appear
    closest_store = closest_stores.iloc[0]
    if units == "km":
        # distance defaulted to km - covert to mi
        closest_store.at['Distance'] = convert_mi_to_km(closest_store['Distance'])

    store_name = closest_store["Store Name"]
    address = ", ".join(
        [closest_store["Address"], closest_store["City"], closest_store["State"], closest_store["Zip Code"]]
    )
    distance = round(closest_store["Distance"], 2)

    # print information to console
    print(f"The closest store is {store_name} at {address}. You are {distance} {units} away from the store.")

    # save to file
    if output:
        # json output
        if output == "json":
            with open("closest_store.json", "w") as f:
                closest_store.to_json(f, indent=4)
        else:
            # text output default
            with open("closest_store.txt", "w") as f:
                closest_store.to_string(f)


if __name__ == "__main__":
    main()
