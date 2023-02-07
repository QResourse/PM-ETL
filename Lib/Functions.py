import requests
import xml.etree.ElementTree as Xet
import base64
from datetime import timedelta, date
import os as _os
import pandas as pd 


def tryToGetAttribute(Object,inputString):
    try:
        output = Object[str(inputString)]
    except:
        output = "Null"
    return output


#used to get the access token
def getToken(USERNAME,PASSWORD):
    AuthStringRaw = USERNAME+":"+PASSWORD
    base64_bytes = AuthStringRaw.encode("ascii")
    authtoken = base64.b64encode(base64_bytes)
    base64_authtoken = authtoken.decode("ascii")
    return base64_authtoken


#Used to get the header of the request
def getHeaderBearer(token):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Requested-With': 'QualysPostman',
    'Authorization': 'Bearer '+ token
    }
    return headers

#Used to get the header of the request
def getHeaderBearerPaging(token,pageSize=100,pageNumber=1):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Requested-With': 'QualysPostman',
    'pageSize': str(pageSize),
    'pageNumber': str(pageNumber),
    'Authorization': 'Bearer '+ token
    }
    return headers

#Used to get the header of the request
def getTokenHeader():
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "X-Requested-With": "QualysPostman",
    }
    return headers

#Used to Post requests
def postRequest(URL,payload,headers,files=[]):
    print("POSTING to "+ URL)
    #print("Payload: "+ str(payload))
    try:
        response = requests.request("POST", URL, headers=headers, data=payload, files=files)
    except:
        print("Failed to send request to API")
        return str(response.status_code)

    if (response.ok != True):
        print("Failed to get response from API")
        return {"Error"}
    else:
        return  response


def getRequest(URL,payload,headers,files=[]):
    print("POSTING to "+ URL)
    print("Payload: "+ str(payload))
    try:
        response = requests.request("GET", URL, headers=headers, data=payload)
    except:
        print("Failed to send request to API")
    
    if (response.ok != True):
        print("Failed to get response from API")
        return {"Error"}
    else:
        return  response


def deleteTempFiles(files):
    for file in files:
        if _os.path.exists(file):
            _os.remove(file)




