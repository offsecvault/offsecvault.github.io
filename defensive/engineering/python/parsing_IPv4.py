#!/bin/python

# It will read a file, collect and parse the following format XXX.XXX.XXX.XXX/XX

import re

filepath = "/home/folder/IPv4_data_to_parse.txt"

file = open(filepath, 'r')
read_exec = file.read()
networks=[]
regex = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,2})',read_exec)

for ip in regex:
    networks.append(ip)
    print(ip)
