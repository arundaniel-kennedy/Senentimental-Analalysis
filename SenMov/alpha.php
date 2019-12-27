<!DOCTYPE html>
<?php
session_start();
?>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <?php include 'includes/header.php'; ?>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <title></title>
  </head>
  <body>
    <?php include 'includes/navbar.php';
    include 'includes/conn.php';

    $sql = "SELECT * FROM ads order by title  limit 50";
    $result = $conn->query($sql);
    ?>

    <div class="container">
      <div class="row pt-5">

      <?php
        if ($result->num_rows > 0) {
          while($row = $result->fetch_assoc()) {
      ?>
        <div class="col pt-3">
          <form action="contentpage.php" method="post">
            <div class="card hvrbox" style="width:12rem;border-radius:0px;height: 38vh;">
              <div class="hvrbox-layer_bottom">
                <img src="http://img.omdbapi.com/?apikey=bb0208a1&i=<?php echo $row['tid'];?>" class="card-img-top" alt="" height="200vh;">
                <div class="card-body ">
                  <?php echo $row['title'];?> <br>
                  <?php echo $row['year'];?>
                </div>
              </div>
              <input name="id" type="text" value="<?php echo $row['tid'];?>" hidden>
              <div class="hvrbox-layer_top">
            		<div class="hvrbox-text">
                  <span class="fas fa-star" style="color:gold;"></span> <br>
                  <?php echo $row['imdb'];?>
                  <br>
                  genre <br>
                  <button class="btn btn-success mt-5" type="submit" name="button">View details</button>
                </div>
            	</div>
            </div>
          </form>
        </div>
      <?php
            }
              } else {
                  echo "0 results";
              } ?>
      </div>
    </div>


    <?php include 'includes/footer.php'; ?>
  </body>
</html>
