#!/bin/bash 

  usename='example_username' # DEFINING THE USERNAME (STRING)

  apikey='example_apikey' # DEFINING THE USERNAME (STRING)

  date=`env LANG="en_US.UTF-8" date -u "+%a, %d %b %Y %H:%M:%S GMT"` # THIS IS DEFINING THE SPECIFIC DATE FORMAT NEEDED FOR THE AUTHENTICATION, 
  # SAVED AS UTF-8 
  
  password=`echo -en "$date" | openssl dgst -sha1 -hmac "$apikey" -binary | openssl enc -base64` # THIS IS GENERATING THE PASSWORD, IT IS PRINTING THE 
  # DATE GENERATED BELOW, ADDING THE HASH GENERATED OF THE API_KEY PRINTED IN BINARY FORMAT, ALL ENCODED IN BASE64

  curl -i --url "http://open.chinanetcenter.com/CloudEye/CeQueryStatisticsSource" \ # URL NEEDED TO MAKE THE API REQUEST

  -X POST \ 

  -u $usename:$password \ 

  -H "Date: $date" \ 

  -H 'Accept: application/json' \ 

  -H 'Content-Type: application/json' \ 

  -d '{"type":"5","dateBegin":"2016-10-08   07:20:02","taskId":"717db918dc514537b65c1f6bf16caa05"}' 

  echo `date` 
