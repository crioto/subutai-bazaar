from subutai_bazaar import rh

class Peer:
    def __init__(self, peer):
        self.__resourceHosts = []
        self.__Version = ''
        self.__IP = ''
        self.__Status = ''
        self.__Scope = ''
        self.__registrationDate = ''
        self.__ownerID = 0
        self.__name = ''
        self.__ownerName = ''
        self.__ID = ''
        if peer['resource_hosts']:
            for r in peer['resource_hosts']:
                nrh = rh.ResourceHost(r)
                self.__resourceHosts.append(nrh)

    def ResourceHosts(self):
        return self.__resourceHosts
