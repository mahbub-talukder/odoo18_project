<?php
$page = 'events';          // used to load home.css
$title = 'Evenements';
include 'includes/header.php';
?>

<main>
    <div style="height: 160px;"></div>

    <div style="min-height: 100vh;">
        <div class="container">

            <div class="events-parent" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">

                <div class="events-parent-child" data-aos="fade-up" data-aos-delay="1500">
                    <h2 data-aos="zoom-in" data-aos-delay="500">
                    <b>Soyez prêts: 
des événements inoubliables arrivent bientôt</b>
                </h2>

                <p data-aos="zoom-out" data-aos-delay="2500">
                    <b>—restez à l'écoute pour les mises à jour !</b>
                </p>
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