#!/bin/python3

import pycurl
import csv

request = pycurl.Curl()
request.setopt(request.URL, 'http://google.com')
request.perform()

effective_url = request.getinfo(pycurl.EFFECTIVE_URL)
name_lookup = request.getinfo(pycurl.NAMELOOKUP_TIME)
connect_time = request.getinfo(pycurl.CONNECT_TIME)
pretransfer_time = request.getinfo(pycurl.PRETRANSFER_TIME)
redirect_time = request.getinfo(pycurl.REDIRECT_TIME)
starttransfer_time = request.getinfo(pycurl.STARTTRANSFER_TIME)
total_time = request.getinfo(pycurl.TOTAL_TIME)
    

header = ['effective_url','namelookup_time','connect_time','pretransfer_time','redirect_time','starttransfer_time','total_time']    
data = [effective_url,name_lookup, connect_time, pretransfer_time, redirect_time, starttransfer_time,total_time]

file = open('Zzz.csv','w+')
action = csv.writer(file)
action.writerow(header)
action.writerow(data)

request.close()
file.close()

