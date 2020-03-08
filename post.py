#!/usr/bin/python
# importing the requests library 
import requests
import json
import xmltodict
import time
from datetime import datetime

url = "https://greenimpulse.org/cgi-bin/receive.py"

while(True):

    with open('/ram/DOA_value.html') as fd:
        data = xmltodict.parse(fd.read())

    data['DATA']['timestamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    # sending post request and saving response as response object 
    r = requests.post(url, data=json.dumps(data), headers=headers)

    time.sleep(1)

