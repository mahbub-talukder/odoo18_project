<?php
// footer.php
?>


  <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
  <footer class=" py-5 shadow-sm">
  <div class="container bg-white">
    <div class="row">
      <!-- 60% Section -->
      <div class="col-12 col-md-7 mb-4 mb-md-0">
        <div class="footer-right-section">
            <div class="footer-logo">
                <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-refined.png" alt="Logo" class="logo-footer" />
            </div>
        <p class="mini-paragraph">
          L'idéologie de <span style="color: #0805b1;"><b>ACP est la social-démocratie.</b></span> Elle désigne un courant politique qui se déclare <span style="color: #ac0306;"><b>réformiste et progressiste</b></span> tout en appliquant des idées positives de la politique libérale.
        </p>
        <p class="mini-paragraph">
            L’A.C.P opte pour des principes fondamentaux de la social-démocratie pour la concrétisation de son idéal caractérisé par :
 <span style="color: #706200;"> <br /><b>Liberté - Justice - Solidarité</b></span>
</p>
        <div class="row">
            <div class="col-12 col-md-6"><a href="mailto:Media@acp.org.cd" class="footer-link"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16">
  <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/>
</svg> media@acp.org.cd</a></div>
            <div class="col-12 col-md-6"><a href="tel:+243819797978" class="footer-link">
             <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.68.68 0 0 0 .178.643l2.457 2.457a.68.68 0 0 0 .644.178l2.189-.547a1.75 1.75 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.6 18.6 0 0 1-7.01-4.42 18.6 18.6 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877z"/>
</svg>   
            +243 817 628 644</a></div>
        </div>
        </div>
      </div>

      <!-- 40% Section -->
      <div class="col-12 col-md-5">
        <div class="row">
            <div class="col-12 col-md-6">
                <h6 class="footer-link-topic">Liens Utiles</h6>
                <ul class="list-unstyled">
                    <li><a href="#" class="footer-link">Qui Sommes-nous?</a></li>
                    <li><a href="#" class="footer-link">Mot de l'autrité morale</a></li>
                    <li><a href="#" class="footer-link">Espace adhérants</a></li>
                    <li><a href="#" class="footer-link">Actualités</a></li>
                    <li><a href="#" class="footer-link">Rejoignez ACP</a></li>
                    <li><a href="#" class="footer-link">28 Mai 2025</a></li>
                    <li><a href="#" class="footer-link">Objectif 2025</a></li>
                    
                </ul>

            </div>

            <div class="col-12 col-md-6">
                <h6 class="footer-link-topic">Social</h6>
                <ul class="list-unstyled">
                    <li><a href="#" class="footer-link">Facebook</a></li>
                    <li><a href="#" class="footer-link">Instagram</a></li>
                    <li><a href="#" class="footer-link">Youtube</a></li>
                    <li><a href="#" class="footer-link">Twitter</a></li>
                    
                </ul>

            </div>

        </div>
      </div>
    </div>
    <hr>

    <div class="row">
        <div class="col-12 col-md-7">
            <p class="text-muted mb-0">&copy; Copyright <?= date('Y') ?> -  Tous droits réservés</p>
            <p class="text-muted">Toutes les images sont la propriété privé de l'Alliance des Congolais Progressistes (ACP). <br /> N’utilisez pas ces images à d'autres fin</p>

        </div>

        <div class="col-12 col-md-5 text-md-end text-center">
  <a href="#" class="footer-link">Mentions Légales</a> &nbsp;&nbsp; | &nbsp; <a href="https://4levels.co.za" class="footer-link">4levels</a>
</div>

    </div>

  </div>
</footer>

  <!-- Bootstrap JS Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-0buJr4I1N7e5b6h5vx7xkBmlVry+0yo8HXELmWzDTnZdhpiVCKUX3vWtuKhPXT/+" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="<?= BASE_URL ?>/assets/css/global.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <script src="<?= BASE_URL ?>/assets/js/global.js"></script>
  <script src="<?= BASE_URL ?>/assets/js/<?= htmlspecialchars($page) ?>.js"></script>
</body>
</html>