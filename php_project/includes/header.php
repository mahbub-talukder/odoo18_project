<?php
// include config for BASE_URL
require_once __DIR__ . '/../config/config.php';

// Set default title if not provided
if (!isset($title)) {
    $title = 'acp';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Your site description here" />
  <meta name="author" content="Thobile" />

  <link rel="icon" type="image/png" href="<?= BASE_URL ?>/assets/img/favicon/refined-logo.png" />

  <title>ACP | <?= htmlspecialchars($title) ?></title>


  <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-XLxJvZUvbsWiIN3okg5HKzJibR5XjvWm/hd3xWZfO2UR8goFzVfUXkaq4WFRzsjV" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">

<!-- AOS CSS -->
  <link 
    href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" 
    rel="stylesheet"
  /> 


  <!-- Global styles -->
  <link rel="stylesheet" href="<?= BASE_URL ?>/assets/css/global.css" />

  <!-- Page specific styles -->
  

  <!-- Google Fonts: Ubuntu -->
  <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">


    
  <?php if (isset($page)): ?>
    <link rel="stylesheet" href="<?= BASE_URL ?>/assets/css/<?= htmlspecialchars($page) ?>.css" />
  <?php endif; ?>

</head>
<body>
  
  <div class="header-wrapper">
    <nav class="red-bar">
      <div class="nav-left">
        <a href="<?= BASE_URL ?>" class="nav-link"><b>ACCUEIL</b></a>
        <a href="<?= BASE_URL ?>about.php" class="nav-link"><b>QUI SOMMES -NOUS</b></a>
        <a href="<?= BASE_URL ?>authors.php" class="nav-link"><b>AUTORITÉ</b></a>
        <a href="<?= BASE_URL ?>#" class="nav-link"><b>ACPIENS</b></a>
      </div>
      <div class="nav-right">
        <a href="<?= BASE_URL ?>deputies.php" class="nav-link"><b>STRUCTURES</b></a>
        <a href="<?= BASE_URL ?>events.php" class="nav-link"><b>ÉVÉNEMENTS</b></a>
        <a href="<?= BASE_URL ?>contact.php" class="nav-link"><b>CONTACTS</b></a>
        <a href="<?= BASE_URL ?>join-the-family.php" class="nav-link"><b>ADHÉSION</b></a>
      </div>
    </nav>
    
    <!--<div class="floating-logo">
      <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-refined.png" alt="Site Logo" class="site-logo" />
    </div>-->
    <div class="floating-logo">
                <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-new.png" alt="Logo" class="" />
            </div>
  </div>

  <!-- Mobile Header -->
<div class="mobile-header">
  <div class="mobile-top-bar">
    <div class="mobile-floating-logo">
      <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-new.png" alt="Logo" />
    </div>
    <button class="hamburger" onclick="toggleMenu()">☰</button>
  </div>

  <div class="mobile-menu" id="mobileMenu">
    <a href="<?= BASE_URL ?>" class="mobile-nav-link">ACCUEIL</a>
    <a href="<?= BASE_URL ?>about.php" class="mobile-nav-link">QUI SOMMES-NOUS</a>
    <a href="<?= BASE_URL ?>authors.php" class="mobile-nav-link">AUTORITE</a>
    <a href="<?= BASE_URL ?>#" class="mobile-nav-link"><b>ACIPIENS</b></a>
    <a href="<?= BASE_URL ?>deputies.php" class="mobile-nav-link"><b>Députés</b></a>
    <a href="<?= BASE_URL ?>events.php" class="mobile-nav-link">EVENEMENTS</a>
    <a href="<?= BASE_URL ?>contact.php" class="mobile-nav-link">CONTACTEZ-NOUS</a>
    <a href="<?= BASE_URL ?>join-the-family.php" class="mobile-nav-link">REJOIGNEZ-NOUS</a>
  </div>
</div>


<script>
  function toggleMenu() {
    const menu = document.getElementById("mobileMenu");
    menu.classList.toggle("active");
  }
</script>
  
  <!-- Spacer so content isn't hidden behind fixed header -->
  