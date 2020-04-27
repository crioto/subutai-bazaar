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
        if rh['rh_cpu_data']:
            if rh['rh_cpu_data']['system']:
                self.__cpuData['system'] = rh['rh_cpu_data']['system']
            if rh['rh_cpu_data']['idle']:
                self.__cpuData['idle'] = rh['rh_cpu_data']['idle']
            if rh['rh_cpu_data']['iowait']:
                self.__cpuData['iowait'] = rh['rh_cpu_data']['iowait']
            if rh['rh_cpu_data']['user']:
                self.__cpuData['user'] = rh['rh_cpu_data']['user']
            if rh['rh_cpu_data']['nice']:
                self.__cpuData['nice'] = rh['rh_cpu_data']['nice']
            if rh['rh_cpu_data']['load']:
                self.__cpuData['load'] = rh['rh_cpu_data']['load']
            if rh['rh_cpu_data']['used']:
                self.__cpuData['used'] = rh['rh_cpu_data']['used']
        if rh['rh_cpu_model']:
            if rh['rh_cpu_model']['frequency']:
                self.__cpuModel['frequency'] = rh['rh_cpu_model']['frequency']
            if rh['rh_cpu_model']['core']:
                self.__cpuModel['core'] = rh['rh_cpu_model']['core']
            if rh['rh_cpu_model']['name']:
                self.__cpuModel['name'] = rh['rh_cpu_model']['name'].strip()
        if rh['rh_disk_data']:
            if rh['rh_disk_data']['total']:
                self.__diskData['total'] = rh['rh_disk_data']['total']
            if rh['rh_disk_data']['available']:
                self.__diskData['available'] = rh['rh_disk_data']['available']
        if rh['rh_disk_model']:
            if rh['rh_disk_model']['total']:
                self.__diskModel['total'] = rh['rh_disk_model']['total']
        if rh['rh_memory_data']:
            if rh['rh_memory_data']['active']:
                self.__memoryData['active'] = rh['rh_memory_data']['active']
            if rh['rh_memory_data']['cached']:
                self.__memoryData['cached'] = rh['rh_memory_data']['cached']
            if rh['rh_memory_data']['mem_free']:
                self.__memoryData['mem_free'] = rh['rh_memory_data']['mem_free']
            if rh['rh_memory_data']['buffers']:
                self.__memoryData['buffers'] = rh['rh_memory_data']['buffers']
            if rh['rh_memory_data']['total_ram']:
                self.__memoryData['total_ram'] = rh['rh_memory_data']['total_ram']
            if rh['rh_memory_data']['available_ram']:
                self.__memoryData['available_ram'] = rh['rh_memory_data']['available_ram']
        if rh['rh_memory_model']:
            if rh['rh_memory_model']['total']:
                self.__memoryModel['total'] = rh['rh_memory_model']['total']
        if rh['rh_net_data']:
            if rh['rh_net_data']['net_in']:
                self.__netData['net_in'] = rh['rh_net_data']['net_in']
            if rh['rh_net_data']['net_out']:
                self.__netData['net_out'] = rh['rh_net_data']['net_out']
        if rh['rh_creation_date']:
            self.__creationDate = rh['rh_creation_date']
        if rh['rh_id']:
            self.__id= rh['rh_id'].strip()
        if rh['rh_name']:
            self.__name = rh['rh_name'].strip()
        if rh['rh_p2p_status']:
            self.__p2pStatus = rh['rh_p2p_status'].strip()
        if rh['rh_p2p_version']:
            self.__p2pVersion = rh['rh_p2p_version'].strip()
        if rh['rh_uptime']:
            self.__uptime= rh['rh_uptime']
        if rh['rh_local_ip']:
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
