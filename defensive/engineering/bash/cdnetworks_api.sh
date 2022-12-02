#!/bin/bash

#..... DEFINING_USER_AUTH:

USER=" "
API_KEY=" "

#..... DATE_IN_RFC_1123_FORMAT_AS_PART_OF_THE_STEP_ TO_GENERATE_THE_PASSWORD:
#>>>>> NOTE: format required is the following: [Thu, 10 Oct 2013 09:12:20 GMT]

DATE=`env LANG="en_US.UTF-8" date -u "+%a, %d %b %Y %H:%M:%S GMT"`

#..... GENERATING_THE_PASSWORD_NEEDED_TO_MAKE_THE_API-CALL:

PASSWORD=$(echo -n "$DATE" | openssl dgst -sha1 -hmac "$API_KEY" -binary | base64)

#..... MENU

clear
read -p "Press [ENTER] key to continue..."
clear

echo -e "\n"
echo -e "PLEASE SELECT AN API CALL ?\n"
echo -e "1. queryCompressionConfig \n"
echo -e "2. QueryCdnDomainService \n"
echo -e "3. QueryRealIpService \n"
echo -e "4. QueryApiDomainListService \n"
echo -e "5. QueryDomainAliasService \n"
echo -e "6. QueryDomainBySrcIpService \n"
echo -e "7. queryHttpcodecacheConfig \n"
echo -e "0. Exit \n"

echo -ne "Choose an option: "
read option

# TITLE: queryCompressionConfig 
# https://documents.cdnetworks.com/document/api-doc/23814
if(("$option" == "1")); then
	echo -ne "insert the domain-name or domain-id: "
	read domain_name_id
	echo -e "\n"
	API_queryCompressionConfig="https://api.cdnetworks.com/api/config/compresssetting/$domain_name_id"
	API_CALL_queryCompressionConfig= curl -i --url $API_queryCompressionConfig \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/xml" \
	-H "x-time-zone:GMT+08:00" \
	-H "Content-Type:application/json"

# TITLE: QueryCdnDomainService
# https://documents.cdnetworks.com/document/api-doc/23809
elif(("$option" == "2")); then
	echo -ne "insert the domain-name or domain-id: "
	read domain_name_id
	echo -e "\n"
	API_QueryCdnDomainService="https://api.cdnetworks.com/cdnw/api/domain/$domain_name_id"
	API_CALL_QueryCdnDomainService= curl -i --url $API_QueryCdnDomainService \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/xml" \
	-H "x-time-zone:GMT+08:00"
	
# TITLE: QueryRealIpService
elif(("$option" == "3")); then
	echo -ne "insert the domain-name or domain-id: "
	read domain_name_id
	echo -e "\n"
    curl -i --url "https://api.cdnetworks.com/api/si/report/whiteip-list?domain=$domain_name_id&viewtype=all&iptype=ipseg" -X "GET" -u "$USER:$PASSWORD" -H "Date: $DATE" -H "Accept: application/json" -H "Content-Type:application/json"

# TITLE: QueryApiDomainListService
# https://documents.cdnetworks.com/document/api-doc/23836
elif(("$option" == "4")); then
	echo -ne "insert the cname-label [domain-name]: "
	read cname_label
	echo -e "\n"
	API_QueryApiDomainListService="https://api.cdnetworks.com/api/domain?cname-label=$cname_label"
	API_CALL_QueryApiDomainListService= curl -i --url $API_QueryApiDomainListService \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/xml" \
	-H "x-time-zone:GMT+08:00"

# TITLE: QueryDomainAliasService
# https://documents.cdnetworks.com/document/api-doc/23998
elif(("$option" == "5")); then
	echo -ne "insert the domain-name or domain-id: "
	read domain_name_id
	echo -e "\n"
	API_QueryDomainAliasService="https://api.cdnetworks.com/api/domain/domain-and-alias/$domain_name_id"
	API_CALL_QueryDomainAliasService= curl -i --url $API_QueryDomainAliasService \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/xml" \
	-H "x-time-zone:GMT+08:00"

# TITLE: QueryDomainBySrcIpService
# https://documents.cdnetworks.com/document/api-doc/24008
elif(("$option" == "6")); then
	echo -ne "insert the origin ip address: "
	read origin_ip
	echo -e "\n"	
	API_QueryDomainBySrcIpService="https://api.cdnetworks.com/api/originaldomainlist?originip=$origin_ip"
	API_CALL_QueryDomainBySrcIpService= curl -i --url $API_QueryDomainBySrcIpService \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/json" \
	-H "x-time-zone:GMT+08:00"

# TITLE: queryHttpcodecacheConfig
# https://documents.cdnetworks.com/document/api-doc/23837
elif(("$option" == "7")); then
	echo -ne "insert the domain-name or domain-id: "
	read domain_name_id
	echo -e "\n"	
	API_queryHttpcodecacheConfig="https://api.cdnetworks.com/api/config/httpcodecache/$domain_name_id"
	API_CALL_queryHttpcodecacheConfig= curl -i --url $API_queryHttpcodecacheConfig \
	-X "GET" \
	-u "$USER:$PASSWORD" \
	-H "x-cnc-date: $DATE" \
	-H "Accept: application/xml" \
	-H "x-time-zone:GMT+08:00"

elif(("$option" == "0"));then
exit 0;

else

echo -e "\n\n"
exit 0;
fi
