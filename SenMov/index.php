<!DOCTYPE html>
<?php session_start(); ?>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <?php include 'includes/header.php'; ?>
    <title></title>
  </head>
  <body style="background-color:black;">
    <?php
    include "includes/navbar.php";
    include 'includes/conn.php';

    ?>

    <div class="container pt-5">

        <center>
          <span class="title">ABH movies</span>
          <span>
            <h2>Welcome to ABH movies. Here you will be able to know the ratings and reviews of the all genre movies in a most predominant way.
          </h2></span>


        <div class="wid text-center">
          <form action="index.html" method="post" style="padding-top:20vh;">
            <div class="form-group">
              <input type="text" name="name" class="form-control" placeholder="Search for movies....">
            </div>
          </form>
        </div>

        </center>
    </div>
    <?php include 'includes/footer.php'; ?>
  </body>
</html>
