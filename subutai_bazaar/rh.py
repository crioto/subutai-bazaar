class ResourceHost:
    def __init__(self, rh):
        self.__cpuData = {'system': 0.0, 'idle': 0.0, 'iowait': 0.0,
                          'user': 0.0, 'nice': 0.0, 'load': 0.0,
                          'user': 0.0}
        self.__cpuModel = {'frequency': '', 'core': '', 'name': ''}
        self.__diskData = {'total': 0.0, 'available': 0.0}
        self.__diskModel = {'total': 0.0}
        self.__memoryData = {'active': 0.0, 'cached': 0.0, 'mem_free': 0.0,
                             'buffers': 0.0, 'total_ram': 0.0,
                             'available_ram': 0.0}
        self.__memoryModel = {'total': 0.0}
        self.__netData = {'net_in': 0.0, 'net_out': 0.0}
        self.__creationDate = ''
        self.__id = ''
        self.__name = ''
        self.__p2pStatus = ''
        self.__p2pVersion = ''
        self.__uptime = 0.0
        self.__localIP = ''
        if 'rh_cpu_data' in rh:
            if 'system' in rh['rh_cpu_data']:
                self.__cpuData['system'] = rh['rh_cpu_data']['system']
            if 'idle' in rh['rh_cpu_data']:
                self.__cpuData['idle'] = rh['rh_cpu_data']['idle']
            if 'iowait' in rh['rh_cpu_data']:
                self.__cpuData['iowait'] = rh['rh_cpu_data']['iowait']
            if 'user' in rh['rh_cpu_data']:
                self.__cpuData['user'] = rh['rh_cpu_data']['user']
            if 'nice' in rh['rh_cpu_data']:
                self.__cpuData['nice'] = rh['rh_cpu_data']['nice']
            if 'load' in rh['rh_cpu_data']:
                self.__cpuData['load'] = rh['rh_cpu_data']['load']
            if 'used' in rh['rh_cpu_data']:
                self.__cpuData['used'] = rh['rh_cpu_data']['used']
        if 'rh_cpu_model' in rh:
            if 'frequency' in rh['rh_cpu_model']:
                self.__cpuModel['frequency'] = rh['rh_cpu_model']['frequency']
            if 'core' in rh['rh_cpu_model']:
                self.__cpuModel['core'] = rh['rh_cpu_model']['core']
            if 'name' in rh['rh_cpu_model']:
                self.__cpuModel['name'] = rh['rh_cpu_model']['name'].strip()
        if 'rh_disk_data' in rh:
            if 'total' in rh['rh_disk_data']:
                self.__diskData['total'] = rh['rh_disk_data']['total']
            if 'available' in rh['rh_disk_data']:
                self.__diskData['available'] = rh['rh_disk_data']['available']
        if 'rh_disk_model' in rh:
            if 'total' in rh['rh_disk_model']:
                self.__diskModel['total'] = rh['rh_disk_model']['total']
        if 'rh_memory_data' in rh:
            if 'active' in rh['rh_memory_data']:
                self.__memoryData['active'] = rh['rh_memory_data']['active']
            if 'cached' in rh['rh_memory_data']:
                self.__memoryData['cached'] = rh['rh_memory_data']['cached']
            if 'mem_free' in rh['rh_memory_data']:
                self.__memoryData['mem_free'] = rh['rh_memory_data']['mem_free']
            if 'buffers' in rh['rh_memory_data']:
                self.__memoryData['buffers'] = rh['rh_memory_data']['buffers']
            if 'total_ram' in rh['rh_memory_data']:
                self.__memoryData['total_ram'] = rh['rh_memory_data']['total_ram']
            if 'available_ram' in rh['rh_memory_data']:
                self.__memoryData['available_ram'] = rh['rh_memory_data']['available_ram']
        if 'rh_memory_model' in rh:
            if 'total' in rh['rh_memory_model']:
                self.__memoryModel['total'] = rh['rh_memory_model']['total']
        if 'rh_net_data' in rh:
            if 'net_in' in rh['rh_net_data']:
                self.__netData['net_in'] = rh['rh_net_data']['net_in']
            if 'net_out' in rh['rh_net_data']:
                self.__netData['net_out'] = rh['rh_net_data']['net_out']
        if 'rh_creation_date' in rh:
            self.__creationDate = rh['rh_creation_date']
        if 'rh_id' in rh:
            self.__id= rh['rh_id'].strip()
        if 'rh_name' in rh:
            self.__name = rh['rh_name'].strip()
        if 'rh_p2p_status' in rh:
            self.__p2pStatus = rh['rh_p2p_status'].strip()
        if 'rh_p2p_version' in rh:
            self.__p2pVersion = rh['rh_p2p_version'].strip()
        if 'rh_uptime' in rh:
            self.__uptime= rh['rh_uptime']
        if 'rh_local_ip' in rh:
            self.__localIP = rh['rh_local_ip'].strip()

    def CPUModel(self):
        return self.__cpuModel

    def CPUData(self):
        return self.__cpuData

    def DiskData(self):
        return self.__diskData

    def DiskModel(self):
        return self.__diskModel

    def MemoryData(self):
        return self.__memoryData

    def MemoryModel(self):
        return self.__memoryModel

    def NetData(self):
        return self.__netData

    def CreationDate(self):
        return self.__creationDate

    def ID(self):
        return self.__id

    def Name(self):
        return self.__name

    def P2PStatus(self):
        return self.__p2pStatus

    def P2PVersion(self):
        return self.__p2pVersion

    def Uptime(self):
        return self.__uptime

    def LocalIP(self):
        return self.__localIP
