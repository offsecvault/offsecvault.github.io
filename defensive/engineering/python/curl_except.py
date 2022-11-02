#!/bin/python3

import pycurl
import csv

http_header = "https://"
filepath = "/home/scripting/sites.csv"

def headers():
    header = ['effective_url','namelookup_time','connect_time','pretransfer_time','redirect_time','starttransfer_time','total_time']
    file = open('Zzz.csv','w+')
    action = csv.writer(file)
    action.writerow(header)

def curl_except(compose_url):

    request = pycurl.Curl()
    request.setopt(request.URL, compose_url)
    request.setopt(request.FOLLOWLOCATION, False)
    request.setopt(request.TIMEOUT, 15)

    try:
        request.perform() 

        effective_url = request.getinfo(request.EFFECTIVE_URL)
        name_lookup = request.getinfo(request.NAMELOOKUP_TIME)
        connect_time = request.getinfo(request.CONNECT_TIME)
        pretransfer_time = request.getinfo(request.PRETRANSFER_TIME)
        redirect_time = request.getinfo(request.REDIRECT_TIME)
        starttransfer_time = request.getinfo(request.STARTTRANSFER_TIME)
        total_time = request.getinfo(request.TOTAL_TIME)

        data = [effective_url,name_lookup, connect_time, pretransfer_time, redirect_time, starttransfer_time,total_time]

        file = open('Zzz.csv','a+')
        action = csv.writer(file)
        action.writerow(data)    
    
    except:
        msg = [compose_url + "____> ERROR_NOT_HANDLED"]
        file = open('Zzz.csv','a+')
        action = csv.writer(file)
        action.writerow(msg)

    request.close()
    file.close() 

def curl_request(compose_url):

    request = pycurl.Curl()
    request.setopt(request.URL, compose_url)
    request.setopt(request.FOLLOWLOCATION, False)
    request.perform()
        
    effective_url = request.getinfo(request.EFFECTIVE_URL)
    name_lookup = request.getinfo(request.NAMELOOKUP_TIME)
    connect_time = request.getinfo(request.CONNECT_TIME)
    pretransfer_time = request.getinfo(request.PRETRANSFER_TIME)
    redirect_time = request.getinfo(request.REDIRECT_TIME)
    starttransfer_time = request.getinfo(request.STARTTRANSFER_TIME)
    total_time = request.getinfo(request.TOTAL_TIME)

    data = [effective_url,name_lookup, connect_time, pretransfer_time, redirect_time, starttransfer_time,total_time]

    file = open('Zzz.csv','a+')
    action = csv.writer(file)
    action.writerow(data)

    request.close()
    file.close()
    
def read_exec():
    
    headers()
    file = open(filepath, 'r')
    
    for url in file:
        current_url = url.strip()
        print(current_url)
        compose_url = http_header + current_url
        curl_except(compose_url)
        #curl_request(compose_url)

### MAIN

def main():
    r = read_exec
    r()

main()
