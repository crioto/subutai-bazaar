import pytest
from context import subutai_bazaar
from subutai_bazaar import bazaar


def test_bazaar_init():
    b1 = bazaar.Bazaar()
    b2 = bazaar.Bazaar('dev')
    b3 = bazaar.Bazaar('master')
    assert b1.url() == 'bazaar.subutai.io'
    assert b2.url() == 'devbazaar.subutai.io'
    assert b3.url() == 'masterbazaar.subutai.io'
