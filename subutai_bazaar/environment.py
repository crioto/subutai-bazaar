from subutai_bazaar import container

class Environment:
    def __init__(self, env):
        self.__key = ""
        self.__id = ""
        self.__status = ""
        self.__statusDesc = ""
        self.__ttl = 0
        self.__p2pSubnet = ""
        self.__hubID = 0
        self.__vni = 0
        self.__cidr = ""
        self.__ownerID = 0
        self.__owner = ""
        self.__name = ""
        self.__hash = ""
        self.__applications = []
        self.__blueprintApps = []
        self.__containers = []
        self.__peers = []
        # TODO: Parse environment_blueprint_apps
        # TODO: Parse environment applications
        # TODO: Parse environment peers
        if 'environment_key' in env:
            self.__key = env['environment_key']
        if 'environment_id' in env:
            self.__id = env['environment_id']
        if 'environment_status' in env:
            self.__status = env['environment_status']
        if 'environment_status_desc' in env:
            self.__statusDesc = env['environment_status_desc']
        if 'environment_ttl' in env:
            self.__ttl = env['environment_ttl']
        if 'environment_p2p_subnet' in env:
            self.__p2pSubnet = env['environment_p2p_subnet']
        if 'hub_id' in env:
            self.__hubID = env['hub_id']
        if 'environment_vni' in env:
            self.__vni = env['environment_vni']
        if 'environment_subnet_cidr' in env:
            self.__cidr = env['environment_subnet_cidr']
        if 'environment_owner_hub_id' in env:
            self.__ownerID= env['environment_owner_hub_id']
        if 'environment_owner' in env:
            self.__owner = env['environment_owner']
        if 'environment_name' in env:
            self.__name= env['environment_name']
        if 'environment_hash' in env:
            self.__hash= env['environment_hash']
        if 'environment_containers' in env:
            for c in env['environment_containers']:
                nc = container.Container(c)
                self.__containers.append(nc)

    def BlueprintApps(self):
        return self.__blueprintApps

    def Key(self):
        return self.__key

    def ID(self):
        return self.__id

    def Status(self):
        return self.__status

    def StatusDesc(self):
        return self.__statusDesc

    def TTL(self):
        return self.__ttl

    def P2PSubnet(self):
        return self.__p2pSubnet

    def HubID(self):
        return self.__hubID

    def VNI(self):
        return self.__vni

    def CIDR(self):
        return self.__cidr

    def OwnerID(self):
        return self.__ownerID

    def Owner(self):
        return self.__owner

    def Applications(self):
        return self.__applications

    def Name(self):
        return self.__name

    def Hash(self):
        return self.__hash

    def Containers(self):
        return self.__containers
