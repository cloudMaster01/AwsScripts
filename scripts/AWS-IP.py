# Check if the input IP is part of which AWS service IP range from https://ip-ranges.amazonaws.com/ip-ranges.json

from netaddr import IPNetwork, IPAddress
import requests
import json

#replace with the IP address you wish to check
IP_TO_CHECK = '52.95.20.249'

data  = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').text
json_data = json.loads(data)
prefixes = json_data['prefixes']
for prefix in prefixes :
    if IPAddress(IP_TO_CHECK) in IPNetwork(prefix['ip_prefix']) :
        #IP address is a member of given prefix
        print(prefix)
