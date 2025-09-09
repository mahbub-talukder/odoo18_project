<?php
$page = 'deputies-individual';          // used to load home.css
$title = 'deputies-individual';
include 'includes/header.php';
?>

<main>
    <div style="height: 160px;"></div>

    <div class="container d-flex justify-content-center align-items-center" style="min-height: 300px;">
  <img src="<?= BASE_URL ?>/assets/img/deputy-profile-icon.png" class="" alt="" style="width: 150px;">
</div>

    <div class="container py-4">

  <!-- First Centered Div -->
  <div class="mb-3 p-3 text-center">
    <h1 class="title">Hon.</h1>
  </div>

  <!-- Second Centered Div -->
  <div class="mb-3 p-3 text-center">
    <h1 class="name">Jean KABILA </h1>
  </div>

  <!-- Third Centered Div -->
  <div class="mb-3 p-3 text-center">
     <p class="position"> Député National</p>
  </div>

  <!-- Fourth Div with Two Side-by-Side Divs (Not Centered) -->
  <div class="p-3">
    <div class="row">
      <div class="col-md-6 mb-2">
        <div class="p-3 text-center">+243 000 000 00</div>
      </div>
      <div class="col-md-6 mb-2">
        <div class="p-3 text-center">jean.kabile@acp-rdc.cd</div>
      </div>
    </div>
  </div>

</div>

<div class="container text-center py-4">
  <div class="mb-3">
    <h2 class="heading-style">BIOGRAPHIE</h2>
  </div>
  <div style="max-width: 600px;">
    <p>Hon. Jean Kabila est Député National au sein de l’Assemblée nationale de la République Démocratique du Congo,
 représentant l’Action Commune pour le Progrès (ACP). Il est titulaire d’une maîtrise en sciences politiques de
 l’Université de Kinshasa. Avant son élection, il a occupé le poste de Directeur de Cabinet au Ministère de l’Intérieur.</p>
  </div>
</div>

<div class="container py-4 d-flex justify-content-center">
  <div class="text-center" style="max-width: 600px;">

    <!-- Topic -->
    <h2 class="mb-4 heading-style"> POINTS FORTS ET CONTRIBUTION</h2>

    <!-- First Section -->
    <div class="mb-4">
      <h4 class="sub-heading-topic"> RÉALISATION 1</h4>
      <p>Nom du projet (2010 – 2014)</p>
      <ul class="list-unstyled">
        <li>• Évalué le projet de force opérationnelle pour l'amélioration du département de la réception</li>
        <li>• Supervisé le processus quotidien des quarts de travail </li>
        <li>• ssuré que tous les membres de l'équipe respectent les procédures opératoires standardisées.</li>
      </ul>
    </div>

    <!-- Second Section -->
    <div>
      <h4 class="sub-heading-topic" style="margin-bottom:30px;"> RÉALISATION 2</h4>
      <p style="margin-bottom: 20px;"> Nom du projet ( 2014 – 2015 )</p>
      <ul class="list-unstyled">
        <li>• Veridies discrepancies and resolves any billing issues in a timely manner</li>
        <li>•  Organizes and maintains accounting records responsible for gathering</li>
      </ul>
    </div>

  </div>
</div>

<div class="container text-center py-5">
  
  <!-- Topic -->
  <h2 class="mb-4 heading-style">ÉDUCATION</h2>
  
  <!-- Six Paragraphs -->
  <p>2003 - 2006</p>
  <p><b> Paucek and Lage University</b></p>
  <p> Bachelor Degree of Hotel Management</p>
  <p><b> 2007 – 2009</b></p>
  <p><b> Fradel and Spies University</b></p>
  <p> Master Degree of Business Administration</p>

</div>

<div class="container d-flex justify-content-center py-5">
  <div class="text-center" style="max-width: 600px;">
    
    <!-- Topic -->
    <h2 class="mb-4 heading-style"> PRINCIPALES RESPONSABILITÉS</h2>

    <!-- First Unordered List -->
    <ul class="list-unstyled">
      <li>• Overseeing accounting and compliance </li>
      <li>• Managing finances and strategic planning</li>
    </ul>

    

  </div>
</div>


    <?php include 'includes/footer.php'; ?>
</main>