import requests
import urllib.parse
import json


class Node:
    def __init__(self, hostname, templateId, peerID, resourceHostID):
        self.hostname = hostname
        self.templateId = templateId
        self.peerID = peerID
        self.resourceHostID = resourceHostID


class Bazaar:

    def __init__(self, host=''):
        if host != '' and host != 'master' and host != 'dev':
            raise Exception('Unknown CDN URL')
        self.url = host+'bazaar.subutai.io'
        self.scheme = 'https://'
        self.session = ''
        self.session_name = 'SUBUTAI_HUB_SESSION'
        return

    def __perform(self, method, endpoint, data=None, headers=None):
        cookies = {}
        if self.session != '':
            cookies = {
                self.session_name: self.session
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
        return urllib.parse.urljoin(self.scheme + self.url, endpoint)

    def Auth(self, username, password):
        self.session = ''
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
                if cookie.name == self.session_name:
                    self.session = cookie.value
                    return True
        return False

    def ListPeers(self, peertype=''):
        if self.session == '':
            raise Exception('Not Authenticated')
        if peertype == '':
            peertype = 'public'

        res = self.__perform("get", "/rest/v1/client/peers/"+peertype)
        if res['status'] == 200:
            return json.loads(res['content'])
        return []

    def CreateEnvironment(self, name, keys, hosts, nodes):
        if self.session == '':
            raise Exception('Not Authenticated')

        nodes = []

        payload = {
            "environmentName": name,
            "exchangeSshKeys": keys,
            "registerHosts": hosts,
            "nodes": nodes
        }

        return
