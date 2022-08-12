import requests
import os
import json
import pandas as pd
import os.path
from os import path
import csv
from pathlib import Path

api_host = 'INSERT THE URL'
api_token = 'INSERT THE API TOKEN'

def make_request(api_path, data):
    url = api_host + api_path
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.post(url, headers=headers, data=data)
    response = r.json()
    if 'Ok' in response:
        return response['Ok']
    else:
        print(response)

def login():
    api_path = 'v1/login'
    data = '{"command":"login", "api_token":"' + api_token + '"}'
    results = make_request(api_path, data)
    flag = False
    if 'token' in results:
        flag = True
        return results['token']  
    return flag

def enumerate_tenants(access_token):
    tenants = []
    api_path = 'v1/customers'
    data = '{"command":"list", "token":"' + access_token + '"}'
    results = make_request(api_path, data)
    for tenant in results:
        t = tenant['name']
        tenants.append(t)
    return tenants

def enumerate_sites(access_token, tenants):
    sites = []
    api_path = 'v2/sites'
    for tenant in tenants:
        data = '{"command":"list", "token":"' + access_token + '", "customer_name": "' + tenant + '"}'
        results = make_request(api_path, data)
        for site in results:
            sites.append(site['hostname'])
    return sites

def enumerate_f_tenants(access_token):
    f_tenants = []
    api_path = 'v1/customers'
    data = '{"command":"list", "token":"' + access_token + '"}'
    results = make_request(api_path, data)
    f_tenants.append(results)
    return f_tenants

def enumerate_f_sites(access_token, tenants):
    f_sites = []
    api_path = 'v2/sites'
    for tenant in tenants:
        data = '{"command":"list", "token":"' + access_token + '", "customer_name": "' + tenant + '"}'
        results = make_request(api_path, data)
        f_sites.append(results)

    return f_sites

def main():
    access_token = login()
    if access_token:
        tenants = enumerate_tenants(access_token)
        sites = enumerate_sites(access_token,tenants)
        
        with open('sites.csv','w',encoding='utf-8') as site:
          for url in sites:
                for row in url:
                    site.write(row)
                site.write("\n")      
         
       # print(" ===== TASK COMPLETED =====")

main()
