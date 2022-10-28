#!/bin/bash

#>>>>> defining the URL of the cdnetwork API call to make
#>>>>> comment/uncomment each time you want to collect different information
#>>>>> create more title section and add the API_URL needed

#TITLE:  

API_URL="type the URL..." 

#defining user auth

USER=""
API_KEY=""

#creating the date in RFC 1123 format as part of the steps to generate the password

DATE='date -u "+%a, %d %b %Y %H:%M:%S %Z"'

#generating the password needed to make the api_call

PASSWORD=$(echo -n "$DATE" | openssl dgst -sha1 -hmac "$API_KEY" -binary | base64)
echo " "

#creating the api_call syntax using curl

API_CALL="curl -i --url $API_URL -X GET -u $USER:$PASSWORD -H 'Date: $DATE' -H 'Accept: application/json'"

#performing the api_call

eval $API_CALL
echo " "
