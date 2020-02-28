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
$ cd find_store/
```
### 2. Install dependencies
```bash
$ pipenv install
$ pipenv shell
```

### 3. Export API key to environment variable
```bash
$ export GOOGLE_API_KEY=<Secret API Key>
```

### 4. Install Application
```bash
$ pipenv install .
```

### 5. Run Application and Usage
```bash
$ find_store --address="<address>"
$ find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
$ find_store --zip=<zip>
$ find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]
```