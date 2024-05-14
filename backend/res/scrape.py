import requests

def networkBypass():
    try:
        result = requests.get("https://steampowered.com")
    except: 
        # if steam dose'nt give a response this means that the network is blocking it
        return False
    return True