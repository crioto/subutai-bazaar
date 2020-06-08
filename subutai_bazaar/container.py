class Container:
    def __init__(self, c):
        self.__state = ""
        self.__size = ""
        self.__ip = ""
        self.__peerID = ""
        self.__name = ""
        self.__rhIP = ""
        self.__hostname = ""
        self.__id = ""
        self.__templateID = ""
        self.__templateName = ""
        if 'container_state' in c:
            self.__state = c['container_state']
        if 'container_size' in c:
            self.__size = c['container_size']
        if 'container_ip' in c:
            self.__ip = c['container_ip']
        if 'container_peer_id' in c:
            self.__peerID = c['container_peer_id']
        if 'container_name' in c:
            self.__name = c['container_name']
        if 'rh_ip' in c:
            self.__rhIP= c['rh_ip']
        if 'container_hostname' in c:
            self.__hostname= c['container_hostname']
        if 'container_id' in c:
            self.__id= c['container_id']
        if 'container_template_id' in c:
            self.__templateID= c['container_template_id']
        if 'container_template_name' in c:
            self.__templateName = c['container_template_name']

    def State(self):
        return self.__state

    def Size(self):
        return self.__size

    def IP(self):
        return self.__ip

    def PeerID(self):
        return self.__peerID

    def Name(self):
        return self.__name

    def RHIP(self):
        return self.__rhIP

    def Hostname(self):
        return self.__hostname

    def ID(self):
        return self.__id

    def TemplateID(self):
        return self.__templateID

    def TemplateName(self):
        return self.__templateName
