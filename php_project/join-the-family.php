<?php
$page = 'join-the-family';          // used to load home.css
$title = 'Rejoingez-nous';
include 'includes/header.php';
?>

<main>
  <div style="height: 160px;"></div>

  <div>
    <div class="image-crop-container">
      <img src="<?= BASE_URL ?>/assets/img/woman-holding-card.png" class="focus-right-image" alt="">
    </div>

    <div class="container card-box" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <div class="cards-parent">
        <img src="<?= BASE_URL ?>/assets/img/front-card.png" class="card-back" alt="" data-aos="zoom-in" data-aos-delay="500" data-aos-duration="1000">
        <img src="<?= BASE_URL ?>/assets/img/back-card.png" class="card-back" alt="" data-aos="zoom-in" data-aos-delay="1000" data-aos-duration="1000">

      </div>
    </div>

    <div class="container bottom-blue" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">

      <div class="bottom-blue-content">
        <p class="bottom-blue-paragraph"><b>Adhérez à l'ACP et découvrez les nombreux avantages de notre programme de membres.</b></p>
        <img src="<?= BASE_URL ?>/assets/img/right-arrow-icon-picture.png" class="icon" alt="">
      </div>

    </div>

  </div>

  <div class="form-big-parent">

    <div class="container">

      <div class="row">
        <div class="col-12 col-md-6 pe-0 pe-md-5" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
          <div class="genity">Une carte, mille opportunités</div>
          <div class="topicstyle-1">Rejoignez la famille</div>
          <div class="d-flex align-items-center gap-3">
            <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-refined.png" alt="Logo" class="small-logo-logo" style="height: 60px;" />

            <div>
              <div class="acp-contain" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
                <div class="letter letter-a">A</div>
                <div class="letter letter-c">C</div>
                <div class="letter letter-p">P</div>
              </div>
            </div>
          </div>
          <div class="paragraph-to-form" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">Adhérez à l'ACP et découvrez les nombreux avantages de notre programme de membres. Votre carte personnelle vous ouvrira les portes à des services de valeur, des réductions chez nos partenaires et la possibilité de participer activement à la croissance de la RDC. Saisissez cette chance de faire partie du changement positif !</div>
        </div>

        <div class="col-12 col-md-6" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000">

          <div>
            <div class="row">
              <div class="col-12 col-md-6 mb-3">
                <label for="input1" class="form-label-custom">Nom</label>
                <input type="text" id="input1" class="form-input-custom" placeholder="">
              </div>

              <div class="col-12 col-md-6 mb-3">
                <label for="input2" class="form-label-custom">Post Nom</label>
                <input type="text" id="input2" class="form-input-custom" placeholder="">
              </div>
            </div>

            <div class="row">
              <div class="col-12 col-md-6 mb-3">
                <label for="input1" class="form-label-custom">Email</label>
                <input type="text" id="input1" class="form-input-custom" placeholder="">
              </div>

              <div class="col-12 col-md-6 mb-3">
                <label for="input2" class="form-label-custom">Telephone</label>
                <input type="text" id="input2" class="form-input-custom" placeholder="">
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label for="input1" class="form-label-custom">Fonction</label>
                <input type="text" id="input1" class="form-input-custom" placeholder="">
              </div>
            </div>

            <div class="row">
              <div class="col-12 col-md-6 mb-3">
                <label for="input1" class="form-label-custom">Sexe</label>
                <input type="text" id="input1" class="form-input-custom" placeholder="">

                <button class="submit-button">Soumettre</button>

              </div>

              <div class="col-12 col-md-6 mb-3" data-aos="fade-top" data-aos-delay="1500" data-aos-duration="1000">
                <img src="<?= BASE_URL ?>/assets/img/new-hand-card-hold.png" class="hand-card" alt="decoration" />
              </div>

            </div>

          </div>

        </div>

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