# solace-env-harness
Harness to quickly create a environment and tear it down. 
Its uses SEMP v2 command
- Create VPN
- Create Queues
- Create Topic Subscription for Queues

# How to configure
Setup the connection string and the credenitial in config.py

 ````
 
Sample Env Definition

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


 ````

# How to run
This is a python3 project

 Execute setupEnv to create the environment
 Execute tearDownEnv to destroy the environment
 