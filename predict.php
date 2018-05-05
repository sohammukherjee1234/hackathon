<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>ONDOC - Predict. Live. Laugh</title>

  <!-- CSS  -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
</head>
<body>
  <nav class="light-blue lighten-1" role="navigation">
    <div class="nav-wrapper container"><a id="logo-container" href="#" class="brand-logo">ONDOC</a>
      <ul class="right hide-on-med-and-down">
        <li><a href="index.php">Home</a></li>
        <li class = "active"><a href="predict.php">Predict</a></li>
        <li><a href="contact.php">Contact Us</a></li>
        
      </ul>

      <ul id="nav-mobile" class="sidenav">
        <li><a href="#">Home</a></li>
      </ul>
      <a href="#" data-target="nav-mobile" class="sidenav-trigger"><i class="material-icons">menu</i></a>
    </div>
  </nav>
  <div class="section no-pad-bot" id="index-banner">
    <div class="container">
      <br><br>
      <h1 class="header center light-blue-text">Select Images to Upload</h1>
      <div class="row center">
<form action="upload.php" method="post" enctype="multipart/form-data">
     <div class="file-field input-field">
      <div class="btn light-blue">
        <span>File</span>
        <input type="file" name="fileToUpload" id="fileToUpload">
      </div>
      <div class="file-path-wrapper">
        <input class="file-path validate" type="text">
      </div>
    </div>
   <br>
   <div class="file-field input-field">
      <div class="btn light-blue">
        <span>File</span>
        <input type="file" name="fileToUpload2" id="fileToUpload2">
      </div>
      <div class="file-path-wrapper">
        <input class="file-path validate" type="text">
      </div>
    </div>

<br>
   <div class="file-field input-field">
      <div class="btn light-blue">
        <span>File</span>
        <input type="file" name="fileToUpload3" id="fileToUpload3">
      </div>
      <div class="file-path-wrapper">
        <input class="file-path validate" type="text">
      </div>
    </div>
    
    
    <br>
   <div class="file-field input-field">
      <div class="btn light-blue">
        <span>File</span>
        <input type="file" name="fileToUpload4" id="fileToUpload4">
      </div>
      <div class="file-path-wrapper">
        <input class="file-path validate" type="text">
      </div>
    </div>


    <input type="submit" class="btn-large waves-effect waves-light light-blue" value="Upload Image" name="submit">
</form>
      </div>
      <br><br>

    </div>
  </div>


  <footer class="page-footer light-blue">
    <div class="container">
      <div class="row">
        <div class="col l6 s12">
          <h5 class="white-text">ONDOC</h5>
          <p class="grey-text text-lighten-4">We are a team of college students working on this project like it's our full time job. Any amount would help support and continue development on this project and is greatly appreciated.</p>


        </div>
       
       </div>
    </div>
    <div class="footer-copyright">
      <div class="container">
      Made by <a class="light-blue-text text-lighten-3" href="#">College Students</a>
      </div>
    </div>
  </footer>


  <!--  Scripts-->
  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script src="js/materialize.js"></script>
  <script src="js/init.js"></script>

  </body>
</html>
