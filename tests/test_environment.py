import pytest
import json
from context import subutai_bazaar
from subutai_bazaar import environment

def test_environment_init():
    data = json.loads('{ \
  "environment_blueprint_apps" : [ ], \
  "environment_key" : "xxxxxx02ef425abe80d2a1cfa72cxxxx", \
  "environment_id" : "822b04e3-9975-4bdb-a17a-0ed03369a12e", \
  "environment_peers" : [ { \
    "peer_prev_state" : "READY", \
    "peer_state" : "READY", \
    "peer_state_time" : "2020-04-20T04:42:04" \
  } ], \
  "environment_status" : "UNHEALTHY", \
  "environment_ttl" : 3600, \
  "environment_p2p_subnet" : "10.103.8.0", \
  "hub_id" : 12177, \
  "environment_status_desc" : "unknown", \
  "environment_vni" : 100014, \
  "environment_subnet_cidr" : "172.19.128.0/24", \
  "environment_owner_hub_id" : 66, \
  "environment_owner" : "Michael De Santa", \
  "environment_applications" : [ ], \
  "environment_name" : "ttt", \
  "environment_hash" : "swarm-822b04e3-9975-4bdb-a17a-0ed03369a12e", \
  "environment_containers" : [ { \
    "container_state" : "RUNNING", \
    "container_size" : "SMALL", \
    "container_ip" : "172.19.128.3", \
    "container_peer_id" : "CB2074DE1C239B59ED3CB53BF8AAF6D6AE7447C7", \
    "container_name" : "Container1-zaj-3-3", \
    "rh_ip" : "10.103.8.1", \
    "container_hostname" : "Container1", \
    "container_id" : "EDE81589DA389B75D5CE877AEBCF99746CD521EE", \
    "container_template_id" : "QmRVDKGX4o2iujuBB5LD9LbC3cMKqYYAk3SNJNT4Rvm", \
    "container_template_name" : "debian-buster" \
  } ] \
}')

    e = environment.Environment(data)
    assert e.Key() == "xxxxxx02ef425abe80d2a1cfa72cxxxx"
    assert e.ID() == "822b04e3-9975-4bdb-a17a-0ed03369a12e"
    assert e.Status() == "UNHEALTHY"
    assert e.TTL() == 3600
    assert e.P2PSubnet() == "10.103.8.0"
    assert e.HubID() == 12177
    assert e.StatusDesc() == "unknown"
    assert e.VNI() == 100014
    assert e.CIDR() == "172.19.128.0/24"
    assert e.OwnerID() == 66
    assert e.Owner() == "Michael De Santa"
    assert e.Name() == "ttt"
    assert e.Hash() == "swarm-822b04e3-9975-4bdb-a17a-0ed03369a12e"
    assert len(e.Containers()) == 1
