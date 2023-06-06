from geo import haversine
from hypothesis import given
from hypothesis.strategies import floats
from numpy import float64


@given(*[floats(-90, 90), floats(-180, 180)] * 2)
def test_haversine(lat1, lng1, lat2, lng2):
    assert type(haversine(lat1, lng1, lat2, lng2)) is float64
