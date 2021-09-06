#!/usr/bin/python
# IoT Chip project version : 3.0

import subprocess as subprocessRef
import json, socket,fcntl,struct
from os.path import split,realpath
import configparser as ConfigParser
import urllib as urllib2
import os
# import urllib2



## Context Path


def write_2_file(data):
    with open(path2_local_storage, "w") as outfile:
        json.dump(data, outfile)

def app_send_json(data):
    path2server_api = "localhost:8000" + "api/blah/get_climate_recipe"
    try:
        print("Sending Data to Server...")
        reqData = urllib2.Request(path2server_api)
        reqData.add_header('Content-Type','application/json')
        respData = urllib2.urlopen(reqData,json.dumps(data)).read()
        print(respData)
    except Exception as e:
    		utils.self.log("Sending Data: "+str(e))

def app_get_json():
    url          = baseUrl+"/api/v1/en/planthive/get-device-command/" + serialNumber
    try :
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        print( json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        write_2_file(data)
    except Exception as e:
        utils.self.log("Server JSON Request: "+str(e))
    except:
        utils.self.log("Server JSON Request: Unknown Error")
    return data
