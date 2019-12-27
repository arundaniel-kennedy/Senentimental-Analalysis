<?php
$user = 'root';
$password = 'root';
$db = 'movies';
$host = 'localhost';
$port = 3306;

$link = mysqli_init();
$conn = new mysqli($host, $user, $password, $db , $port);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
