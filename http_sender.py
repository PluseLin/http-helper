import requests
import json

def sendGetRequest(url:str,data)->tuple:
    ret_data=None
    try:
        with requests.get(url,timeout=3) as r:
            ret_data=(True,r.text)
    except Exception as e:
            ret_data=(False,None)
    return ret_data

def sendPostRequest(url:str,data)->tuple:
    ret_data=None
    try:
        with requests.post(url,json=data,timeout=3) as r:
            ret_data=(True,r.text)
    except Exception as e:
            ret_data=(False,None)
    return ret_data

def sendPutRequest(url:str,data)->tuple:
    ret_data=None
    try:
        with requests.put(url,json=data,timeout=3) as r:
            ret_data=(True,r.text)
    except Exception as e:
            ret_data=(False,None)
    return ret_data

def sendDeleteRequest(url:str,data)->tuple:
    ret_data=None
    try:
        with requests.delete(url,json=data,timeout=3) as r:
            ret_data=(True,r.text)
    except Exception as e:
            ret_data=(False,None)
    return ret_data

post_data={
    "username":"Lin",
    "password":"123"
}

if __name__=="__main__":
    #ret=sendGetRequest("http://127.0.0.1:8000/getUserInfo_Lin")
    ret=sendPostRequest("http://127.0.0.1:8000/userLogin",post_data)
    print(ret)
    