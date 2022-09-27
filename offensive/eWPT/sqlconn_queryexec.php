<?php

$dbhostname='8.8.8.8';
$dbuser = 'username';
$dbpassword = 'password';
$dbname = 'database';

$connection = mysqli_connect($$dbhostname, $dbuser, $dbpassword, $dbname);
$query = "SELECT Name, Description FROM Products WHERE ID='2' UNION SELECT Username, Password FROM Accounts;";

$results = mysqli_query($connection, $query);
display_results($results);
?>
