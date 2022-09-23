#!/bin/python3

import pycurl
import csv

http_header = "http://"
filepath = "/home/scripting/test.csv"

def curl_request(compose_url):

    #print(url_compose)

    request = pycurl.Curl()
    request.setopt(request.URL, compose_url)
    #request.setopt(request.URL, 'https://google.com')
    request.perform()

    effective_url = request.getinfo(request.EFFECTIVE_URL)
    name_lookup = request.getinfo(request.NAMELOOKUP_TIME)
    connect_time = request.getinfo(request.CONNECT_TIME)
    pretransfer_time = request.getinfo(request.PRETRANSFER_TIME)
    redirect_time = request.getinfo(request.REDIRECT_TIME)
    starttransfer_time = request.getinfo(request.STARTTRANSFER_TIME)
    total_time = request.getinfo(request.TOTAL_TIME)

    header = ['effective_url','namelookup_time','connect_time','pretransfer_time','redirect_time','starttransfer_time','total_time']
    data = [effective_url,name_lookup, connect_time, pretransfer_time, redirect_time, starttransfer_time,total_time]

    file = open('Zzz.csv','a+')
    action = csv.writer(file)
    action.writerow(header)
    action.writerow(data)

    request.close()
    file.close()

def read():

    file = open(filepath, 'r')

    for url in file:
        current_url = url.strip()
        print(current_url)
        compose_url = http_header + current_url
        curl_request(compose_url)

### MAIN

def main():
    r = read
    r()
    #c = curl_request
    #c()

main()
