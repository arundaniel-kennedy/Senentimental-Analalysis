<?php

include 'includes/conn.php';

$tid = $_POST["id"];
$comments = $_POST["comment"];

//echo $tid,$comments;

$sql = "INSERT INTO comment (id,comment) VALUES ('$tid','$comments')";

$result = $conn->query($sql);

if($result){
  echo '<script type="text/javascript"> window.alert("success!");</script>';

  header("refresh:0.001;url=highrate.php");
}
else{
  echo '<script type="text/javascript"> window.alert("Error!");</script>';

  header("refresh:0.001;url=highrate.php");
}

?>
