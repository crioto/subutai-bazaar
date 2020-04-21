import pytest
import subutai_bazaar

def test_bazaar_init():
    b1 = subutai_bazaar.Bazaar()
    b2 = subutai_bazaar.Bazaar('dev')
    b3 = subutai_bazaar.Bazaar('master')
    assert b1.url() == 'bazaar.subutai.io'
    assert b2.url() == 'devbazaar.subutai.io'
    assert b3.url() == 'masterbazaar.subutai.io'
