<?php

$dbhostname='8.8.8.8'; #ip address db server
$dbuser = 'username'; #username
$dbpassword = 'password'; #password
$dbname = 'database'; #database name

$connection = mysqli_connect($$dbhostname, $dbuser, $dbpassword, $dbname);
$query = "SELECT Parameter1, Parameter2 FROM table_name WHERE condition UNION SELECT Parameter1, Parameter2 FROM table_name;";

$results = mysqli_query($connection, $query);
display_results($results);
?>
