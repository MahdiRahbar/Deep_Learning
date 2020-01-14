# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:30:32 2020

@author: Mahdi Rahbar
"""

def callApi(url, data, tokenKey):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + tokenKey,
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=data.encode("utf-8"), headers=headers)
    return response.text