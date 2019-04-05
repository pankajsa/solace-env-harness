import requests
import json
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
import urllib.parse


import config as cfg

baseurl = cfg.host + "/SEMP/v2/config/"

def encodeUrl(url):
    return urllib.parse.quote(url,safe='')


class EventManager:

    def __init__(self):
        self._setupSession()
    
    def _setupSession(self):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
        self.session.headers.update({'cache-control': 'no-cache'})
        self.session.auth = (cfg.auth['user'], cfg.auth['password'])
        self.baseurl = baseurl 

    def listVpns(self):
        data = self.doIt("get", "msgVpns", {}, "select=msgVpnName,enabled")
        print("List of MessageVPNs:",data)

    def createVpn(self, avpnName):
        vpnName = encodeUrl(avpnName)

        payload = {
            'msgVpnName': vpnName,
            'enabled': True
        }
        data = self.doIt("post", "msgVpns", payload)
        print("VPN Created:",avpnName)

    def deleteVpn(self, avpnName):
        vpnName = encodeUrl(avpnName)

        data = self.doIt("delete", "msgVpns/" + vpnName)
        # print("MsgVPNs:",data)
        print("VPN Deleted:",avpnName)

    def listQs(self, avpnName):
        vpnName = encodeUrl(avpnName)

        data = self.doIt("get", "msgVpns/" + vpnName + "/queues", 
            {}, "select=queueName")
        print("List of Queues in VPN:",avpnName)
        print(data)




    def createQ(self, avpnName, aq):
        vpnName = encodeUrl(avpnName)
        q = encodeUrl(aq)

        payload = {
            'msgVpnName': vpnName,
            'queueName': q,
            'accessType': 'non-exclusive',
            'egressEnabled': True,
            'ingressEnabled': True,
            'permission': 'consume',
            'respectTtlEnabled': True
        }
        data = self.doIt("post", "msgVpns/" + vpnName + "/queues", payload)
        print("Queue Created in " + avpnName + ":" + aq)

    def deleteQ(self, avpnName, aq):
        vpnName = encodeUrl(avpnName)
        q = encodeUrl(aq)

        data = self.doIt("delete", 
            "msgVpns/" + vpnName + "/queues/" + q)
        print("Queue Deleted in " + avpnName + ":" + aq)

    def showQSubscriptions(self, avpnName, aq):
        vpnName = encodeUrl(avpnName)
        q = encodeUrl(aq)

        data = self.doIt("get", "msgVpns/" + vpnName + "/queues/" + q  + "/subscriptions", 
            {}, "") # select=queueName")
        print("Subscription List for " + q + ":" + aq)
        print(data)


    def addQSubscription(self, avpnName, aq, topic):
        vpnName = encodeUrl(avpnName)
        q = encodeUrl(aq)

        payload = {
            'msgVpnName': vpnName,
            'queueName': q,
            'subscriptionTopic': topic,
        }
        data = self.doIt("post", 
            "msgVpns/" + vpnName + "/queues/" + q  + "/subscriptions", 
            payload)

        print("Subscription Added for " + aq + ":" + topic)


    def deleteQSubscription(self, avpnName, aq, atopic):
        vpnName = encodeUrl(avpnName)
        q = encodeUrl(aq)
        topic = encodeUrl(atopic)

        data = self.doIt("delete", 
            "msgVpns/" + vpnName + "/queues/" + q  + "/subscriptions/" + topic)
        print("QSubscriptions:",data)


    def doIt(self, method = "get", url = "/", payload = {}, path = ""):

        try:
            fullurl = self.baseurl + url + "?" + path
            # fullurl = self.baseurl + url 

            if method == 'get':
                # print('get')
                response = self.session.get(fullurl)
            elif method == 'post':
                # print('post')
                # print("Url" , fullurl)
                # print("payload" , payload)
                # print("payload" , json.dumps(payload))

                # fullurl = 'https://httpbin.org/post'
                response = self.session.post(fullurl, json = payload)
                # print(response.text)
            elif method == 'put':
                # print('put')
                pass
            elif method == 'delete':
                # print('delete')
                response = self.session.delete(fullurl)

            else:
                print('not implemented')

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')  # Python 3.6
            print(f'HTTP error details: {http_err.response.text}')  # Python 3.6
            # print(f'HTTP error occurred: {http_err.text}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            # print('Success!')
            # print(response.text)
            myres = response.json()
            # print("==========")
            # print(myres)
            # print("==========")
            if method == 'get' or method == 'post':
                data = myres['data']
            else:
                data = {}
            # print(data)
            return(data)


