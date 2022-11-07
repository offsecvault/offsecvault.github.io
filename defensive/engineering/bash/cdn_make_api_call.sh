#!/bin/bash

#>>>>> defining the URL of the cdnetwork API call to make
#>>>>> comment/uncomment each time you want to collect different information
#>>>>> create more title section and add the API_URL needed

#..... DEFINING_USER_AUTH:

USER=""
API_KEY=""

#..... LIST_OF_API_URLS_TO_CALL:

#TITLE:  

API_URL="type the URL..." 

#..... DATE_IN_RFC_1123_FORMAT_AS_PART_OF_THE_STEP_ TO_GENERATE_THE_PASSWORD:
#>>>>> NOTE: format required is the following: [Thu, 10 Oct 2013 09:12:20 GMT]

DATE=`env LANG="en_US.UTF-8" date -u "+%a, %d %b %Y %H:%M:%S GMT"`

#generating the password needed to make the api_call

PASSWORD=$(echo -n "$DATE" | openssl dgst -sha1 -hmac "$API_KEY" -binary | base64)

#..... CREATING_THE_API-CALL_SYNTAX_USING_CURL:

#TITLE: CONFIG
API_CALL="curl -i --url $API_URL_CONFIG \
-X GET \
-u $USER:$PASSWORD \
-H 'x-cnc-date: $DATE' \
-H 'Accept: application/json' \
-H 'x-time-zone:GMT+08:00'"

#..... PERFORMING_THE_API-CALL:

eval $API_CALL
echo " "
