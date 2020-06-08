import requests
import urllib.parse

class Client:
    def __init__(self, url='', scheme='https'):
        self.__url = url
        self.__scheme = scheme
        self.__session = ''
        self.__sessionName = ''
        return

    def Perform(self, method, endpoint, data=None, headers=None, files=None):
        cookies = {}
        if self.__session != '':
            cookies = {
                self.__session_name: self.__session
            }
        if method == "get":
            return self.__get(endpoint, data, headers, cookies, files)
        elif method == "post":
            return self.__post(endpoint, data, headers, cookies, files)
        elif method == "put":
            return self.__put(endpoint, data, headers, cookies, files)
        elif method == "delete":
            return self.__delete(endpoint, data, headers, cookies, files)
        else:
            return

    def __get(self, endpoint, data, headers, cookies, files):
        print(self.__buildURL(endpoint))
        res = requests.get(self.__buildURL(endpoint), data=data,
                           headers=headers, cookies=cookies, files=files)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __post(self, endpoint, data, headers, cookies, files):
        res = requests.post(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies, files=files)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __put(self, endpoint, data, headers, cookies, files):
        res = requests.put(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies, files=files)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __delete(self, endpoint, data, headers, cookies, files):
        res = requests.delete(self.__buildURL(endpoint), data=data,
                            headers=headers, cookies=cookies, files=files)
        return {'status': res.status_code, 'content': res.content,
                'headers': res.headers, 'cookies': res.cookies}

    def __buildURL(self, endpoint):
        return urllib.parse.urljoin(self.__scheme + '://' +
                                    self.__url, endpoint)

