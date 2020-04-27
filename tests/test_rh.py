import pytest
import json
from context import subutai_bazaar
from subutai_bazaar import rh

def test_rh_init():
    data = json.loads('{"rh_cpu_model": {"frequency": 3392, "core": 2, "name": " Intel Xeon E3-12xx v2 (Ivy Bridge)"}, "rh_disk_model": {"total": 523234390835.0}, "rh_disk_data": {"total": 523234390835.0, "available": 517543559168.0}, "rh_memory_data": {"active": 1453363572.3636363, "cached": 1771768738.909091, "mem_free": 2022715764.3636363, "buffers": 119898112.0, "total_ram": 6113001472.0, "available_ram": 3791167488.0}, "rh_creation_date": "2018-08-01T05:20:42", "rh_p2p_status": "WORKS", "rh_net_data": {"net_in": 7096.413333333333, "net_out": 12232.213333333333}, "rh_memory_model": {"total": 6113001472.0}, "rh_id": "725D9B074DAACBD553DB1402CC08293A8C9A8906", "rh_name": "subutai", "rh_p2p_version": "8.3.1+201902221002982", "rh_uptime": 0.0, "rh_local_ip": "192.168.1.127", "rh_cpu_data": {"system": 2.5516666666666667, "idle": 93.6, "iowait": 3.6066666666666665, "user": 2.5716666666666668, "nice": 0.0, "load": 0.05006677741945993, "used": 6.400000000000006}}')
    t = rh.ResourceHost(data)
    cpuModel = t.CPUModel()
    assert cpuModel['frequency'] == 3392
    assert cpuModel['core'] == 2
    assert cpuModel['name'] == 'Intel Xeon E3-12xx v2 (Ivy Bridge)'
    cpuData = t.CPUData()
    assert cpuData['system'] == 2.5516666666666667
    assert cpuData['idle'] == 93.6
    assert cpuData['iowait'] == 3.6066666666666665
    assert cpuData['user'] == 2.5716666666666668
    assert cpuData['nice'] == 0.0
    assert cpuData['load'] == 0.05006677741945993
    assert cpuData['used'] == 6.400000000000006
    diskData = t.DiskData()
    assert diskData['total'] == 523234390835.0
    assert diskData['available'] == 517543559168.0
    diskModel = t.DiskModel()
    assert diskModel['total'] == 523234390835.0
    memoryData = t.MemoryData()
    assert memoryData['active'] == 1453363572.3636363
    assert memoryData['cached'] == 1771768738.909091
    assert memoryData['mem_free'] == 2022715764.3636363
    assert memoryData['buffers'] == 119898112.0
    assert memoryData['total_ram'] == 6113001472.0
    assert memoryData['available_ram'] == 3791167488.0
    memoryModel = t.MemoryModel()
    assert memoryModel['total'] == 6113001472.0
    netData = t.NetData()
    assert netData['net_in'] == 7096.413333333333
    assert netData['net_out'] == 12232.213333333333
    assert t.CreationDate() == '2018-08-01T05:20:42'
    assert t.ID() == '725D9B074DAACBD553DB1402CC08293A8C9A8906'
    assert t.Name() == 'subutai'
    assert t.P2PStatus() == 'WORKS'
    assert t.P2PVersion() == '8.3.1+201902221002982'
    assert t.Uptime() == 0.0
    assert t.LocalIP() == '192.168.1.127'

