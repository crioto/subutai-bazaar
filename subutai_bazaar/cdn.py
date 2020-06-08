from subutai_bazaar import client
import subprocess
import json
import gnupg

class CDN:
    def __init__(self, host='', gpg='/usr/bin/gpg', user=None, fingerprint=None):
        self.__host = host
        self.__user = user
        self.__gpg = gpg
        self.__fingerprint = fingerprint
        return

    def Upload(self, filepath):
        if self.__user == None:
            raise Exception('Bazaar user not provided')
        if self.__fingerprint == None:
            raise Exception('GPG fingerprint not provided')
        authID = self.__authID()
        if authID == None:
            raise Exception('Failed to retrieve Auth ID')
        token = self.__token(authID)
        if token == None:
            raise Exception('Failed to retrieve token')
        c = client.Client(self.__host)
        print(token)
        with open(filepath, 'rb') as f:
            res = c.Perform("post",
                            "/rest/v1/cdn/uploadRaw",
                            headers={"token": token},
                            data={"token": token},
                            files={"file": f})
            if res['status'] == 200:
                return json.loads(res['content'])
            else:
                raise Exception('Received status ' + res['status'] + ': ' +
                                res['content'].decode('utf-8'))
        return None

    def Download(self, filename):
        return

    def Delete(self, filename):
        return

    def Info(self, filename):
        c = client.Client(self.__host)
        res = c.Perform('get', '/rest/v1/cdn/raw?name='+filename+'&latest')
        if res['status'] == 200:
            return json.loads(res['content'])
        return None

    def __get(self, endpoint, data, headers, cookies):
        return

    def __authID(self):
        if self.__fingerprint == None:
            raise Exception('authid: no fingerprint')
        c = client.Client(self.__host)
        res = c.Perform('get', '/rest/v1/cdn/token?fingerprint='+
                        self.__fingerprint)
        if res['status'] == 201:
            return res['content'].decode('utf-8')
        return None

    def __token(self, authID):
        if self.__checkGPG == False:
            return None

        gpg = gnupg.GPG()
        signed = gpg.sign(str(authID), keyid=self.__user)

        c = client.Client(self.__host)
        print(signed)
        res = c.Perform("post", "/rest/v1/cdn/token", data={'request': signed})
        if res['status'] == 201:
            return res['content'].decode('utf-8')
        return None

    def __checkGPG(self):
        return True
