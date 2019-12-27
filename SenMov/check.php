<?php
session_start();

include 'includes/conn.php';

$name = $_POST["name"];
$comments = $_POST["comment"];

//echo $tid,$comments;

$sql = "INSERT INTO comment (id,comment) VALUES ('$tid','$comments')";

$result = $conn->query($sql);

if($result){
  $_SESSION["user"] = "validuser";

  echo '<script type="text/javascript"> window.alert("user login success,exiting....!");</script>';

  header("refresh:0.001;url=highrate.php");
}
else{
  echo '<script type="text/javascript"> window.alert("Error!");</script>';

  header("refresh:0.001;url=highrate.php");
}


?>
