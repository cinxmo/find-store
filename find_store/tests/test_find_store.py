import json
import pytest

from find_store import util, get_closest_stores, convert_mi_to_km


@pytest.fixture()
def palo_alto_lat_long():
    with open("find_store/tests/palo_alto_location.json", "r") as f:
        data = json.load(f)
    return data["lat"], data['lng']


def test_verify_zip():
    # test bad zip
    bad_zip = "3333"  # only 4 digits
    assert util.valid_zip(bad_zip) is False

    # test good zip
    good_zip = "94305"
    assert util.valid_zip(good_zip) is True

    # test good zip+4
    good_zip = "94305-1000"
    assert util.valid_zip(good_zip) is True


def test_get_closest_store(palo_alto_lat_long):
    closest_store = get_closest_stores(palo_alto_lat_long[0], palo_alto_lat_long[1]).iloc[0]
    assert closest_store["Store Name"] == "Mountain View"


def test_convert_mi_to_km():
    mile = 1
    assert round(convert_mi_to_km(mile), 4) == 1.6093
