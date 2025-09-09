<?php
$page = 'about';          // used to load home.css
$title = 'about';
include 'includes/header.php';
?>

<?php
$executive_team = [
    ['name' => 'Charles', 'surname' => 'MBUTAMUNTU', 'position' => 'secrétaire général', 'picture' => null],
    ['name' => 'Pius', 'surname' => 'KANDOLO', 'position' => 'SGA Questions Politiques et Implantations', 'picture' => 'images/jane.jpg'],
    ['name' => 'Leaticia', 'surname' => 'BENA KABAMBA', 'position' => 'SGA', 'picture' => 'images/john.jpg'],
    ['name' => 'Albert', 'surname' => 'BOMBITO', 'position' => 'SGA', 'picture' => null],
    ['name' => 'Ketsia', 'surname' => 'OLANGI', 'position' => 'Présidente de la ligue des femmes', 'picture' => null],
    ['name' => 'Moise', 'surname' => 'MUPATA', 'position' => 'Président de la ligue des jeunes', 'picture' => null],
    ['name' => 'Mathieu', 'surname' => 'MUPATA', 'position' => 'Directeur de cabinet Politique', 'picture' => null],
    ['name' => 'Madeleine', 'surname' => 'Luzayadio', 'position' => 'SN InTech', 'picture' => null],
];
?>

<main>

    <div style="height: 160px;"></div>

    <div class="first-parent">
  <div class="container my-5">
    <div class="row text-center">
      
      <!-- Title Column -->
      <div class="col-12 col-md-4 mb-3 mb-md-0 d-flex justify-content-center align-items-center flex-column">
        <h2 class="nous sommes"><b>Nous Sommes</b></h2>
        <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
      </div>

      <!-- Image Column -->
      <div class="col-12 col-md-4 mb-3 mb-md-0 d-flex justify-content-center align-items-center">
        <img src="<?= BASE_URL ?>/assets/img/about-three.png" class="about-three" alt="">
      </div>

      <!-- Text Column -->
      <div class="col-12 col-md-4 d-flex justify-content-center align-items-center">
        <div class="about-text-things d-flex justify-content-center">
            <div class="d-flex justify-content-center">
                <div class="acp-container">
  <span class="letter-a">A</span>
  <span class="letter-c">C</span>
  <span class="letter-p">P</span>
</div>
            </div>
        <p class="mb-0 text-acp">
            
          L'ACP se donne la responsabilité de promouvoir sa trilogie qui se définit par la justice-liberté-travail au sein de la nation congolaise.
        </p>
        </div>
      </div>

    </div>




    <div class="row text-center">
      
      <!-- Title Column -->
      

      <!-- Image Column -->
      <div class="col-12 mb-3 mb-md-0 d-flex justify-content-center align-items-center">
        <a href="#" class="rejoindre"><b>rejoindre l'acp</b></a>
      </div>

      <!-- Text Column -->
      

    </div>




  </div>
</div>

    <div class="container second-parent">
  <div class="row align-items-center">
    <div class="col-12 col-md-6"> 
      <h3 class="topicstyle-1">SINGA NA TONGA</h3>   
      <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
      <h6 class="tozali">
        <b>Tozali singa oyo ezali kolanda tonga.</b>
      </h6>
      <h6 class="tozali">
        <b>NGOBILA MBAKA.</b>
      </h6>
      <p class="tozali-p">Atalisi biso nzela oyo ekokumba baye bandimeli makanisi na ye na bomoko na tina ya kozala batu balingi kimia na limemia kati na bango po na kotombola ekolo na biso.</p>
    </div>

    <div class="col-12 col-md-6">
      <img src="<?= BASE_URL ?>/assets/img/multiple-photos.png" class="multiple-photos" alt="">
    </div>
  </div>
</div> <!-- Fixed closing tag -->

    <div class="container third-parent">
  <div class="row align-items-stretch" style="min-height: 200px;">
    
    <!-- Left Side -->
    <div class="col-12 col-md-6 d-flex flex-column justify-content-center third-parent-left-side">
      <div>
        <div style="margin-bottom: 100px;">
            <h2><b>VISION de l'ACP</b></h2>
            <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
        </div>

        <p class="vision-paragraph">
          Faire de tout Congolais un acteur actif sur le terrain et un élément de changement organique positif dans sa vie quotidienne.
        </p>
      </div>
    </div>

    <!-- Right Side -->
    <div class="col-12 col-md-6 d-flex align-items-center">
      <img src="<?= BASE_URL ?>/assets/img/people-clapping.png" class="vision-picture img-fluid" alt="">
    </div>

  </div>
</div>


<div class="fourth-parent d-flex align-items-center">

        <div class="container">
            <div class="row align-items-center">
                <div class="col-12 col-md-4 "><div class="line-container text-center my-4">
  <h3 class="notre"><b>NOTRE OBJECTIF</b></h3>
  <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
</div></div>
                <div class="col-12 col-md-4"><img src="<?= BASE_URL ?>/assets/img/man-in-blue-2.png" class="vision-picture" alt=""></div>
                <div class="col-12 col-md-4">
                    
                <p><b>ACP est un parti qui s'inscrit dans la durabilité dans le sens intemporel pour des objectifs réels et sérieux.</b></p>

                <p>Inonder les urnes afin de représenter les congolais et concrétiser leurs idées au niveau national et international; aussi nous pousser à comprendre que le progrès débute par un renouvellement de l'intelligence et de connaissance de ce que nous sommes et de ce que nous avons à offrir à l'autre ainsi qu'à l'environnement.</p>

                </div>
            </div>    
        </div>

    </div>

    <div class="fifth-parent">

        
        
            <div class="container executive-team-parent">
                <div class="executive-team d-flex align-items-center justify-content-center">

                    <div class="topic-box">
                        <h2 class="topicstyle-1 text-center">L'équipe Exécutif</h2>
                        <p class="text-center">We’re a creative design studio crafting standout brands and digital experiences. From logos to web design, our work combines strategy and artistry to bring your vision to life.</p>
                
                    </div>

                    </div>
            </div>

            <div class="container executive-team-list py-4">
                <div class="row">
                    <?php foreach ($executive_team as $member): ?>
                        <div class="col-6 col-md-3 mb-4">
                            <div class="team-card">
                                <div class="team-img-wrapper">
                                    <?php if ($member['picture']): ?>
                                        <img src="<?= htmlspecialchars($member['picture']) ?>" alt="Profile of <?= htmlspecialchars($member['name']) ?>">
                                    <?php else: ?>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="#ccc" viewBox="0 0 16 16">
                                            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0-0.001-6.001A3 3 0 0 0 8 8z"/>
                                        </svg>
                                    <?php endif; ?>
                                </div>
                                <div class="team-name"><?= htmlspecialchars($member['name']) ?></div>
                                <div class="team-surname"><?= strtoupper(htmlspecialchars($member['surname'])) ?></div>
                                <div class="team-position"><?= htmlspecialchars($member['position']) ?></div>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            </div>

        

    </div>


    <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>

    <?php include 'includes/footer.php'; ?>
</main>