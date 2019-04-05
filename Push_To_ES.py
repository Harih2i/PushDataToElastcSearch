# -------------------------------------------------------------------------------
# Name:        Data_Push_To_ElasticSearch.py
# Purpose:     Data to push into ElasticSearch with Python
#
# Author:      Hari Krishna Misra
# Created:     02/13/2019
# -------------------------------------------------------------------------------

import requests
import datetime

KIBANA_IP = "100.97.59.63"
API_INDEX = "demo_index"
API_TYPE = "demo_type"

KIBANA_API = "http://"+KIBANA_IP+":9200/"+API_INDEX+"/"+API_TYPE
headers = {'Content-type': 'application/json'}
payload = {
	"FirstName":"Hari",
	"LastName":"Misra",
	"Role":"CEO",
	"timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
	}

created_res = requests.post(KIBANA_API, json=payload,headers=headers, verify = False, timeout=60)

if created_res.status_code == 201:
	print "Record has been successfully created into ICEMAN"
else:
	print "Creation failed and Status code:", created_res.status_code
