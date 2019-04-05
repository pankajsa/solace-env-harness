from EventManager import EventManager



vpnName = 'nse_vpn'

def setupEnv():    
    em = EventManager()
    em.listVpns()
    em.createVpn(vpnName)
    em.createQ(vpnName, "q1")
    em.addQSubscription(vpnName,"q1", "a/b")
    em.addQSubscription(vpnName,"q1", "d/>")

def tearDownEnv():    
    em = EventManager()
    em.deleteQ(vpnName, "q1")
    em.deleteVpn(vpnName)


setupEnv()
tearDownEnv()

# em.addQSubscription(vpnName,"q1", "a/b")
# em.showQSubscriptions(vpnName,"q1")
# em.deleteQSubscription(vpnName,"q1", 'a%2Fb')
# em.showQSubscriptions(vpnName,"q1")

# em.listQs(vpnName)

# em.deleteQ(vpnName, "q1")
# em.deleteVpn(vpnName)

# em.createQ("test1", "q4")
# em.deleteQ("test1", "q4")
# em.deleteVpn("test1")
# em.createVpn("test1")
# em.createQ("test1", "q4")
# em.listQs("test1")
# em.showQSubscriptions("test1","q4")
# print("=========")
# em.addQSubscription("test1","q4", "g/1")
# print("=========")
# em.addQSubscription("test1","q4", "g/2")
# print("=========")
# encoded = urllib.parse.quote("b/*/c",safe='')
# print(encoded)

# em.deleteQSubscription("test1","q4", encodeUrl('d/>'))

# em.showQSubscriptions("test1","q4")

# em.listVpns()
# em.deleteVpn("test1")
# em.listVpns()
