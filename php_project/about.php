<?php
$page = 'about';          // used to load home.css
$title = 'Qui Sommes -Nous';
include 'includes/header.php';
?>

<?php

  $member = [
    'name' => 'Charles',
    'surname' => 'MBUTAMUNTU',
    'position' => 'Secrétaire général',
    'picture' => null // or null if no picture
];


$executive_team = [
    /**['name' => 'Charles', 'surname' => 'MBUTAMUNTU', 'position' => 'secrétaire général', 'picture' => null] */
    ['name' => 'Pius', 'surname' => 'KANDOLO', 'position' => 'SGA Questions Politiques et Implantations', 'picture' => null],
    ['name' => 'Leaticia', 'surname' => 'BENA KABAMBA', 'position' => 'SGA', 'picture' => null],
    ['name' => 'Albert', 'surname' => 'BOMBITO', 'position' => 'SGA', 'picture' => null],
    ['name' => 'Ketsia', 'surname' => 'OLANGI', 'position' => 'Présidente de la ligue des femmes', 'picture' => null],
    ['name' => 'Moise', 'surname' => 'MUPATA', 'position' => 'Président de la ligue des jeunes', 'picture' => null],
    ['name' => 'Mathieu', 'surname' => 'MUPATA', 'position' => 'Directeur de cabinet Politique', 'picture' => null],
    ['name' => 'Madeleine', 'surname' => 'Luzayadio', 'position' => 'SN InTech', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
];
?>

<main>

    <div style="height: 160px;"></div>

    <div class="first-parent">
  <div class="container my-5">
    <div class="row text-center">
      
      <!-- Title Column -->
      <div class="col-12 col-md-4 mb-3 mb-md-0 d-flex justify-content-center align-items-center flex-column" data-aos="fade-down" data-aos-delay="500" data-aos-duration="500">
        <h2 class="nous sommes"><b>Nous Sommes</b></h2>
        <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
      </div>

      <!-- Image Column -->
      <div class="col-12 col-md-4 mb-3 mb-md-0 d-flex justify-content-center align-items-center" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000">
        <img src="<?= BASE_URL ?>/assets/img/president-in-white.png" class="about-three" alt="">
      </div>

      <!-- Text Column -->
      <div class="col-12 col-md-4 d-flex justify-content-center align-items-center" data-aos="fade-down" data-aos-delay="1500" data-aos-duration="1000">
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
        <a href="<?= BASE_URL ?>join-the-family.php" class="rejoindre" data-aos="zoom-in" data-aos-delay="2000" data-aos-duration="3000"><b>rejoignez l'acp</b></a>
      </div>

      <!-- Text Column -->
      

    </div>




  </div>
</div>

    <div class="container second-parent">
  <div class="row align-items-center">
    <div class="col-12 col-md-6"> 
      <div class="d-inline-block">
        <h3 class="topicstyle-1 d-inline-block" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">SINGA NA TONGA</h3>   
      <div class="line-something my-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
      </div>
      <h6 class="tozali" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
        <b>Tozali singa oyo ezali kolanda tonga.</b>
      </h6>
      <h6 class="tozali" data-aos="fade-down" data-aos-delay="1000" data-aos-duration="1000">
        <b>NGOBILA MBAKA.</b>
      </h6>
      <p class="tozali-p">Atalisi biso nzela oyo ekokumba baye bandimeli makanisi na ye na bomoko na tina ya kozala batu balingi kimia na limemia kati na bango po na kotombola ekolo na biso.</p>
    </div>

    <div class="col-12 col-md-6" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">
      <img src="<?= BASE_URL ?>/assets/img/multiple-photos.png" class="multiple-photos" alt="">
    </div>
  </div>
</div> <!-- Fixed closing tag -->

    <div class="container third-parent">
  <div class="row align-items-stretch" style="min-height: 200px;">
    
    <!-- Left Side -->
    <div class="col-12 col-md-6 d-flex flex-column justify-content-center third-parent-left-side" data-aos="zoom-in" data-aos-delay="500" data-aos-duration="1000">
      <div>
        <div style="margin-bottom: 100px;" class="d-inline-block">
            <h2 class="d-inline-block" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000"><b>VISION de l'ACP</b></h2>
            <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
        </div>

        <p align="justify" data-aos="zoom-in" data-aos-delay="500" data-aos-duration="1000">
          Nous aspirons à faire de chaque Congolais un acteur actif et engagé dans son environnement, capable d'initier et de promouvoir un changement organique positif dans sa vie quotidienne.
Nous croyons fermement que chaque individu, en tant que membre de notre parti, a le potentiel d'influencer son entourage et de contribuer à un avenir meilleur pour notre pays.
En cultivant une culture de participation, de créativité et de solidarité, nous souhaitons encourager chaque Congolais à prendre des initiatives, à s'impliquer dans des actions communautaires et à défendre l'unité nationale, des valeurs de progrès et de justice.
Ensemble, nous bâtirons une nation où chacun se sentira valorisé et où le changement est le fruit d'un engagement collectif.

        </p>
      </div>
    </div>

    <!-- Right Side -->
    <div class="col-12 col-md-6" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">

  <!-- Image -->
  <div class="text-center mb-4">
    <img src="<?= BASE_URL ?>/assets/img/yellow-background-picture.png" class="vision-picture img-fluid" alt="">
  </div>

  <!-- Content Below the Image -->
  <div style="width: 100%; z-index: 2; margin-top: -210px;">
  <div style="width: 90%; margin: 0 auto;">
    <div class="row g-1"> <!-- g-3 adds gutter spacing -->

      <!-- Box 1 -->
      <div class="col-4">
        <div class="p-1 bg-white rounded text-center">
          <H1 style="color: blue;"><b>99%</b></H1>

          <p>Capacité de mobilisation</p>
        </div>
      </div>

      <!-- Box 2 -->
      <div class="col-4">
        <div class="p-1 bg-white rounded text-center">
          <H1 style="color: brown;"><b>93%</b></H1>
          <p>Présence en RDC</p>
        </div>
      </div>

      <!-- Box 3 -->
      <div class="col-4">
        <div class="p-1 bg-white rounded text-center">
          <H1 style="color: yellow;"><b>50%</b></H1>
          <p>Présence à l'étranger</p>
        </div>
      </div>

    </div>
  </div>
</div>

</div>

  </div>
</div>


<div class="fourth-parent d-flex align-items-center">

        <div class="container">
            <div class="row align-items-center">
                <div class="col-12 col-md-4 " data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
                  <div class="line-container text-center my-4 d-inline-block">
  <h3 class="notre d-inline-block"><b>NOTRE OBJECTIF</b></h3>
  <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
</div>
</div>
                <div class="col-12 col-md-4" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000"><img src="<?= BASE_URL ?>/assets/img/man-in-blue-2.png" class="vision-picture" alt=""></div>
                <div class="col-12 col-md-4" data-aos="fade-down" data-aos-delay="1500" data-aos-duration="1000">
                    
                <p><b>ACP est un parti qui s'inscrit dans la durabilité dans le sens intemporel pour des objectifs réels et sérieux.</b></p>

                <p>L’Objectif général de l’ACP est de conquérir le pouvoir politique, de l’exercer et de le conserver le plus longtemps possible par la voie démocratique. 100% statut !!!!</p>

                </div>
            </div>    
        </div>

    </div>

    <div class="fifth-parent">

        
        
            <div class="container executive-team-parent">
                <div class="executive-team d-flex align-items-center justify-content-center">

                    <div class="topic-box">
                        <h2 class="topicstyle-1 text-center">L'équipe Exécutif</h2>
                        <p class="text-center">Chaque membre de notre équipe apporte une expertise unique et un engagement fort envers nos valeurs et nos objectifs. Ensemble, nous travaillons à bâtir un avenir meilleur pour tous.</p>
                
                    </div>

                    </div>
            </div>

            <div class="container d-flex justify-content-center align-items-center" style="min-height: 200px;">
  <div class="team-card" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
    <div class="team-img-wrapper">
        <?php if (!empty($member['picture'])): ?>
            <img src="<?= htmlspecialchars($member['picture']) ?>" alt="Profile of <?= htmlspecialchars($member['name']) ?>">
        <?php else: ?>
            <img src="<?= BASE_URL ?>/assets/img/logo-thumbnail.png" alt="Default profile picture">
        <?php endif; ?>
    </div>
    <div class="team-name"><?= htmlspecialchars($member['name']) ?></div>
    <div class="team-surname"><?= strtoupper(htmlspecialchars($member['surname'])) ?></div>
    <div class="team-position"><?= htmlspecialchars($member['position']) ?></div>
</div>
</div>

            <div class="container executive-team-list py-4">
              <hr>
                <div class="row">
                    <?php foreach ($executive_team as $member): ?>
                        <div class="col-6 col-md-3 mb-4">
                            <div class="team-card">
                                <div class="team-img-wrapper">
                                    <?php if ($member['picture']): ?>
                                        <img src="<?= htmlspecialchars($member['picture']) ?>" alt="Profile of <?= htmlspecialchars($member['name']) ?>">
                                    <?php else: ?>
                                        <img src="<?= BASE_URL ?>/assets/img/logo-thumbnail.png" class="" alt="">
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


    

    <?php include 'includes/footer.php'; ?>

    <!-- AOS JS --> 
  <script 
    src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js">
  </script>
  <script>
    AOS.init({
      duration: 800,
      once: true,
      offset: 100,
    });
  </script>


</main>