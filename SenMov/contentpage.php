<?php
session_start();

include 'includes/conn.php';

$tid = $_POST["id"];
$sum = 0;

$sql ="SELECT id FROM review ORDER BY RAND() limit 20";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()){
    $sum += $row["id"];
  }
}
else{
  echo "0 results";
}

$rating = ($sum /20)*100;
//echo $rating;

$sql = "UPDATE `ads` SET `rating` = '$rating' WHERE `ads`.`tid` = '$tid'";
$result = $conn->query($sql);


$sql = "SELECT * FROM ads where tid='".$tid."'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        //echo "id: " . $row["tid"]. " Name: " . $row["title"]. " year" . $row["year"]. "<br>";


 ?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <?php
    include 'includes/header.php';
    include 'includes/navbar.php';
    ?>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

    <title></title>
  </head>
  <body>
    <div class="container" style="margin-top:100px;">
      <center>
        <div class="row">

          <div class="col-4 pt-3">
            <div class="card" style="width: 20rem; height:24rem;">
             <img class="card-img-top" src="http://img.omdbapi.com/?apikey=bb0208a1&i=<?php echo $row['tid'];?>" alt="">
            </div>
          </div>

          <div class="col-4 pt-3" style="text-align:left;">
             <h1><?php echo $row['title'];?></h1>
             <br><br>
             <h3>genre</h3>
             <br>
             <h3><span class="fas fa-star" style="color:gold;"></span> <?php echo $row['imdb'];?></h3>
             <h3><span class="fas fa-star" style="color:red;"></span> <?php echo $row['rating'];?>%</h3>

          </div>
          <?php if($_SESSION["user"]==="validuser"){ ?>
          <div class="col-4 pt-3">
            <div class="container">
              <form action="add.php" method="post">
                <div class="form-group"style="width:20rem;">
                  <label for="comment">Comment:</label>
                  <input type="text" name="id" value="<?php echo $row['tid']?>" hidden/>
                  <textarea class="form-control" rows="5" name="comment"></textarea>
                  <br>
                  <button type="submit" class="btn btn-success">Submit</button>
                </div>
              </form>
            </div>
          </div>
        <?php }else{ ?>

          <div class="col-4 pt-3">
            <div class="container">
              <form action="check.php" method="post">
                <h3>Sign in to comment</h3> <br><br>
                <div class="form-group"style="width:20rem;">
                  <label for="name">name:</label>
                  <input type="text" name="id" value="<?php echo $row['tid']?>" hidden/>
                  <input type="text" name="name" class="form-control"  />
                  <label for="password">password:</label>
                  <input type="password" name="name" class="form-control"  />
                  <br>
                  <button type="submit" class="btn btn-success">Submit</button>
                </div>
              </form>
            </div>
          </div>

          <?php
        }
        }
          } else {
              echo "0 results";
          }
         ?>
        </div>
      </center>
    </div>
    <?php include 'includes/footer.php'; ?>
  </body>
</html>
