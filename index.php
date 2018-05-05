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
        <li class = "active"><a href="index.php">Home</a></li>
        <li ><a href="predict.php">Predict</a></li>
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
      
    </div>
  </div>



  <div class="slider">
    <ul class="slides">
      <li>
        <img src="12.jpg"> <!-- random image -->
        <div class="caption right-align">
          <h3>AI</h3>
          <h5 class="light white-text text-lighten-3">Live. Laugh. Predict.</h5>
        </div>
      </li>
      <li>
        <img src="13.jpg"> <!-- random image -->
        <div class="caption right-align">
          <h3>Predicts your Health</h3>
          <h5 class="light white-text text-lighten-3">Only in 3 simple steps</h5>
        </div>
      </li>
      
    </ul>
  </div>




  <div class="container">
    <div class="section">

      <!--   Icon Section   -->
      <div class="row">
      <h5 class="center">Our Work Process</h5>
        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">add_a_photo</i></h2>
            <h5 class="center">Upload Images</h5>

            <p class="light">We did most of the heavy lifting for you to provide a platform where you just need to upload four CTSCAN/MRI/X-Ray images in our website.</p>
          </div>
        </div>

        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">autorenew</i></h2>
            <h5 class="center">AI Prediction </h5>

            <p class="light">By utilizing the CTSCAN/MRI/X-Ray images, our trained AI Algorithm will scan through the images and find the disease user is suffering from (if any).</p>
          </div>
        </div>

        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">remove_red_eye</i></h2>
            <h5 class="center">Name of Disease</h5>

            <p class="light">The name of the disease will be displayed within 30 seconds to the user.</p>
          </div>
        </div>
      </div>

    </div>
    <br><br>
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
<script>$(document).ready(function(){
  $('.slider').slider();
});</script>
  </body>
</html>
