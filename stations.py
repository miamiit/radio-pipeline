import requests

API = "https://de1.api.radio-browser.info/json/stations/search"
HEADERS = {"User-Agent": "radio-pipeline-learning/0.1"}


def get_stations(countrycode, tag, limit=5):
    params = {
        "countrycode": countrycode,
        "tag": tag,
        "hidebroken": "true",
        "order": "votes",
        "reverse": "true",
        "limit": limit,
    }
    resp = requests.get(API, params=params, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    for station in get_stations("GB", "pop"):
        print(station["name"], "|", station["country"], "|", station["tags"], "|", station["url_resolved"])