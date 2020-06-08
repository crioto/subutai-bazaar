import pytest
import json
from context import subutai_bazaar
from subutai_bazaar import container

def test_container_init():
    data = json.loads('{"container_state" : "RUNNING", \
    "container_size" : "SMALL", \
    "container_ip" : "172.19.128.3", \
    "container_peer_id" : "CB2074DE1C239B59ED3CB53BF8AAF6D6AE7447C7", \
    "container_name" : "Container1-zaj-3-3", \
    "rh_ip" : "10.103.8.1", \
    "container_hostname" : "Container1", \
    "container_id" : "EDE81589DA389B75D5CE877AEBCF99746CD521EE", \
    "container_template_id" : "QmRVDKGX4o2iujuBBPqS5LD9LbC3cMKqYYAk3SNJNT4Rvm", \
    "container_template_name" : "debian-buster"}')

    c = container.Container(data)
    assert c.State() == "RUNNING"
    assert c.Size() == "SMALL"
    assert c.IP() == "172.19.128.3"
    assert c.PeerID() == "CB2074DE1C239B59ED3CB53BF8AAF6D6AE7447C7"
    assert c.Name() == "Container1-zaj-3-3"
    assert c.RHIP() == "10.103.8.1"
    assert c.Hostname() == "Container1"
    assert c.ID() == "EDE81589DA389B75D5CE877AEBCF99746CD521EE"
    assert c.TemplateID() == "QmRVDKGX4o2iujuBBPqS5LD9LbC3cMKqYYAk3SNJNT4Rvm"
    assert c.TemplateName() == "debian-buster"
