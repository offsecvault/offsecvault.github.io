#!/bin/bash

clear
read -p "Press [Enter] key to continue..."
clear

echo -e "\n"
echo -e "What test you want to run ?\n"
echo -e "1. APACHE BENCH\n"
echo -e "2. CURL\n"
echo -e "3. APACHE JMETER\n"
echo -e "0. EXIT\n"

echo -ne "CHOOSE AN OPTION: "
read option

if(("$option" == "1")); then

echo -ne "type how many REQUEST: "
read request

echo -ne "type how many CONCURRENT CONNECTIONS: "
read conn

echo -ne "SITE TO TEST: "
read site
echo -e "\n"

ab -n $request -c $conn $site

elif(("$option" == "2")); then

echo -ne "SITE TO TEST: "
read site

date
echo -e "\n"
curl -w @- -v --trace-time -o /dev/null -s "$site" << 'EOF'

time_namelookup: %{time_namelookup} seg\n
time_connect: %{time_connect} seg\n
time_appconnect: %{time_appconnect} seg\n
time_pretransfer: %{time_pretransfer} seg\n
time_redirect: %{time_redirect} seg\n
time_starttransfer: %{time_starttransfer} seg\n
http_code: %{http_code}\n
http_connect: %{http_connect} seg\n
local_ip: %{local_ip}\n
local_port: %{local_port}\n
num_connects: %{num_connects}\n
remote_ip: %{remote_ip}\n
remote_port: %{remote_port}\n
response_code: %{response_code}\n
url_effective: %{url_effective}\n

===========\n

time_total: %{time_total} seg\n
EOF

elif(("$option" == "0"));then
exit 0;

else

echo -e "\n\n"
exit 0;
fi

