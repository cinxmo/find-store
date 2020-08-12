# Command Line Application for Finding Nearest Store

##  Prerequisites
### Google API
1. Go to https://developers.google.com/maps/documentation/geocoding/start to create account
2. Select "Geocoding API"
3. Retrieve the API key

## Installation
### 1. Clone repo
```bash
$ git clone git@github.com:cinxmo/find-store.git
$ cd find-store/
```

### 2. Set environment variables
At the root directory, create an `.env` file and set 
```
GOOGLE_API_KEY=<Secret API Key>
DEBUG=true
```
Note: setting DEBUG to false means that the package is not editable (changes to .py modules in find_store after the 
initial install will NOT be reflected)

### 3. Install app and dependencies
```bash
$ pipenv shell
$ pipenv install
```

### 4. Run Application and Usage
```bash
$ find_store --address="<address>"
$ find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
$ find_store --zip=<zip>
$ find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]
```

### 5. Results
The closest store's name, address, and distance are printed to the console.
A file is automatically saved as `closest_store.txt` unless output is specified as json.

## Run tests 
```bash
$ pipenv install --dev
$ pytest
```

## Assumptions and Explanation
This is a command line application that takes in an address or zip code and prints the name, address, and distance
of the closest store listed in `store-locations.csv`. A text/json file is saved in the root directory depending on
the `--output` option.

### Assumptions
While there is a validity check for zip code based on regular expressions, there is none based on address. 
The assumption is that address input is a string and formatted according to `<Address>, <City>, <State>` and 
could include `<Zip>` at the end as well.

Another assumption is that the user only inputs `km` or `mi` for `--units`, and `json` or `text` for `--output`.
If given more time, we should add additional validation functions in `util.py`.

Distance between two latitude, longitude points is calculated using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).
The assumption is that the radius of the Earth is 3958.8 miles.

If given more time, we should increase the test coverage to include:

- Additional bad zip codes
- Calling the Google Geocoder API with invalid/incomplete addresses (ignored this time since calling API for testing could be costly)
- Add additional fixtures for different addresses/zip codes
- Mock errors thrown from Geocoder and handle the errors appropriately so they don't impact user experience