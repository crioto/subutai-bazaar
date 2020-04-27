from subutai_bazaar import rh

class Peer:
    def __init__(self, peer):
        self.__resourceHosts = []
        self.__version = ''
        self.__ip = ''
        self.__status = ''
        self.__scope = ''
        self.__registrationDate = ''
        self.__ownerID = 0
        self.__name = ''
        self.__ownerName = ''
        self.__id = ''
        if 'resource_hosts' in peer:
            for r in peer['resource_hosts']:
                nrh = rh.ResourceHost(r)
                self.__resourceHosts.append(nrh)
        if 'peer_version' in peer:
            self.__version = peer['peer_version']
        if 'peer_ip' in peer:
            self.__ip = peer['peer_ip']
        if 'peer_status' in peer:
            self.__status = peer['peer_status']
        if 'peer_scope' in peer:
            self.__scope = peer['peer_scope']
        if 'peer_registration_date' in peer:
            self.__registrationDate = peer['peer_registration_date']
        if 'peer_owner_id' in peer:
            self.__ownerID = peer['peer_owner_id']
        if 'peer_name' in peer:
            self.__name = peer['peer_name'].strip()
        if 'peer_owner_name' in peer:
            self.__ownerName = peer['peer_owner_name'].strip()
        if 'peer_id' in peer:
            self.__id = peer['peer_id']


    def ResourceHosts(self):
        return self.__resourceHosts

    def Version(self):
        return self.__version

    def IP(self):
        return self.__ip

    def Status(self):
        return self.__status

    def Scope(self):
        return self.__scope

    def RegistrationDate(self):
        return self.__registrationDate

    def OwnerID(self):
        return self.__ownerID

    def Name(self):
        return self.__name

    def OwnerName(self):
        return self.__ownerName

    def ID(self):
        return self.__id
