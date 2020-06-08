import pytest
import os.path
import yaml
from context import subutai_bazaar
from subutai_bazaar import bazaar


# Functions runs full testing flow
def test_full():
    if not os.path.isfile("config.yaml"):
        print("Skipping full feature test")
        return
    try:
        with open('config.yaml', 'rb') as f:
            cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print("Failed to parse configuration")
        assert not True
    except:
        print("Failed to read configuration")
        assert not True

    username = cfg['username']
    password = cfg['password']

    b = bazaar.Bazaar('dev')

    assert b.Auth(username, password) == True
    favorites = b.ListPeers("favorite")
    for fav in favorites:
        assert b.RemovePeerFromFavorites(fav) == True

    public = b.ListPeers()

    # This may fail if dev bazaar have no public peers
    assert len(public) > 0
    assert b.AddPeerToFavorites(public[0]) == True
    # This may fail if test user have zero balance
    assert b.GetBalance() > 0.0
    envs = b.ListEnvironments()
    print(envs)


def test_bazaar_init():
    b1 = bazaar.Bazaar()
    b2 = bazaar.Bazaar('dev')
    b3 = bazaar.Bazaar('master')
    assert b1.url() == 'bazaar.subutai.io'
    assert b2.url() == 'devbazaar.subutai.io'
    assert b3.url() == 'masterbazaar.subutai.io'
