import requests
import urllib.parse
import json
from subutai_bazaar import peer


class Node:
    def __init__(self, hostname, templateId, peerID, resourceHostID):
        self.__hostname = hostname
        self.__templateId = templateId
        self.__peerID = peerID
        self.__resourceHostID = resourceHostID


class Bazaar:
    def __init__(self, host=''):
        if host != '' and host != 'master' and host != 'dev':
            raise Exception('Unknown CDN URL')
        self.__url = host+'bazaar.subutai.io'
        self.__scheme = 'https://'
        self.__session = ''
        self.__session_name = 'SUBUTAI_HUB_SESSION'
        return

    def url(self):
        return self.__url

    def __perform(self, method, endpoint, data=None, headers=None):
        cookies = {}
        if self.__session != '':
            cookies = {
                self.__session_name: self.__session
            }
        if method == "get":
            return self.__get(endpoint, data, headers, cookies)
        elif method == "post":
            return self.__post(endpoint, data, headers, cookies)
        elif method == "put":
            return self.__put(endpoint, data, headers, cookies)
        elif method == "delete":
            return self.__delete(endpoint, data, headers, cookies)
        else:
            return

    def __get(self, endpoint, data, headers, cookies):
        res = requests.get(self.__buildURL(endpoint), data=data,
                           headers=headers, cookies=cookies)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __post(self, endpoint, data, headers, cookies):
        res = requests.post(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __put(self, endpoint, data, headers, cookies):
        res = requests.post(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __delete(self, endpoint, data, headers, cookies):
        res = requests.post(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __buildURL(self, endpoint):
        return urllib.parse.urljoin(self.__scheme + self.__url, endpoint)

    def Auth(self, username, password):
        self.__session = ''
        payload = {
            'email': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        res = self.__perform("post", "/rest/v1/client/login", payload, headers)
        if res['status'] == 200:
            for cookie in res['cookies']:
                if cookie.name == self.__session_name:
                    self.__session = cookie.value
                    return True
        return False

    def ListPeers(self, peertype=''):
        if self.__session == '':
            raise Exception('Not Authenticated')
        if peertype == '':
            peertype = 'public'

        res = self.__perform("get", "/rest/v1/client/peers/"+peertype)
        if res['status'] == 200:
            peers = json.loads(res['content'])
            result = []
            for p in peers:
                np = peer.Peer(p)
                result.append(np)
            return result
            #return json.loads(res['content'])
        return []

    def CreateEnvironment(self, name, keys, hosts, nodes):
        if self.__session == '':
            raise Exception('Not Authenticated')

        nodes = []

        payload = {
            "environmentName": name,
            "exchangeSshKeys": keys,
            "registerHosts": hosts,
            "nodes": nodes
        }

        return

    def AddPeerToFavorites(self, peerID):
        if self.__session == '':
            raise Exception('Not Authenticated')
        res = self.__perform("put", "/rest/v1/client/peers/favorite/"+peerID)
        if res['status'] == 200:
            return True
        return False

    def RemovePeerFromFavorites(self, peerID):
        if self.__session == '':
            raise Exception('Not Authenticated')
        res = self.__perform("delete", "/rest/v1/client/peers/favorite/"+peerID)
        if res['status'] == 200:
            return True
        return False

