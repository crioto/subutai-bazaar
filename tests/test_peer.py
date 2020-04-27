import pytest
import json
from context import subutai_bazaar
from subutai_bazaar import peer

def test_peer_init():
    data = json.loads('{"resource_hosts": [{"rh_cpu_model": {"frequency": 3392, "core": 2, "name": " Intel Xeon E3-12xx v2 (Ivy Bridge)"}, "rh_disk_model": {"total": 523234390835.0}, "rh_disk_data": {"total": 523234390835.0, "available": 517543559168.0}, "rh_memory_data": {"active": 1453363572.3636363, "cached": 1771768738.909091, "mem_free": 2022715764.3636363, "buffers": 119898112.0, "total_ram": 6113001472.0, "available_ram": 3791167488.0}, "rh_creation_date": "2018-08-01T05:20:42", "rh_p2p_status": "WORKS", "rh_net_data": {"net_in": 7096.413333333333, "net_out": 12232.213333333333}, "rh_memory_model": {"total": 6113001472.0}, "rh_id": "725D9B074DAACBD553DB1402CC08293A8C9A8906", "rh_name": "subutai", "rh_p2p_version": "8.3.1+201902221002982", "rh_uptime": 0.0, "rh_local_ip": "192.168.1.127", "rh_cpu_data": {"system": 2.5516666666666667, "idle": 93.6, "iowait": 3.6066666666666665, "user": 2.5716666666666668, "nice": 0.0, "load": 0.05006677741945993, "used": 6.400000000000006}}], "peer_version": "8.3.2-SNAPSHOT", "peer_ip": "158.181.154.85", "peer_status": "OFFLINE", "peer_scope": "PUBLIC", "peer_registration_date": "2018-08-01T05:20:38", "peer_owner_id": 338, "peer_name": "qavms-kg7_dev2", "peer_owner_name": "QualityA", "peer_id": "E03AD66AFCCD8C1C6AB6B0130F6504C2C2610FC1"}')

    p = peer.Peer(data)
    assert len(p.ResourceHosts()) == 1
    assert p.Version() == '8.3.2-SNAPSHOT'
    assert p.IP() == '158.181.154.85'
    assert p.Status() == 'OFFLINE'
    assert p.Scope() == 'PUBLIC'
    assert p.RegistrationDate() == '2018-08-01T05:20:38'
    assert p.OwnerID() == 338
    assert p.Name() == 'qavms-kg7_dev2'
    assert p.OwnerName() == 'QualityA'
    assert p.ID() == 'E03AD66AFCCD8C1C6AB6B0130F6504C2C2610FC1'
