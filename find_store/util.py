import re


def valid_zip(zip):
    """
    :param zip: zip code to be verified
    :return: boolean - True if it is a valid zip code, False otherwise
    """
    zip_pattern = "^[0-9]{5}(?:-[0-9]{4})?$"
    result = re.match(zip_pattern, zip)
    return True if result else False


def convert_mi_to_km(mi):
    """
    :param km: distance in kilometers
    :return: distance in miles
    """
    return mi / 0.621371
