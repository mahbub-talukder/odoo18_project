<?php
$page = 'contact';          // used to load home.css
$title = 'contact';
include 'includes/header.php';
?>

<main style="background: linear-gradient(to bottom,#ffffff,rgb(225, 223, 223), #ffffff, #c8c8c8);">
    <div style="height: 160px;"></div>

    <div>

        <div class="container">
            <div class="row">
                <div class="col-12 col-md-6">
                
                    <div class="contact-topic-box">
                        <h3 class="contact-topic"><b>Contactez-nous</b></h3>
                        <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
                    </div>

                    <p class="contact-paragraph">Que vous ayez des questions sur nos initiatives, besoin de soutien, ou souhaitiez partager vos commentaires, notre équipe dédiée est là pour vous assister à chaque étape.</p>

                    <div class="contact-info container">
  <div class="row">
    <!-- Email -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/email-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Email</div>
        <div class="text-icon">Media@acp.org.cd</div>
      </div>
    </div>

    <!-- Website -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/email-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Website</div>
        <div class="text-icon">WWW.ACP.ORG.CD</div>
      </div>
    </div>

    <!-- Phone -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3">
      <span class=" icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/email-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Phone</div>
        <div class="text-icon">+243 819 797 978</div>
      </div>
    </div>

    <!-- Location -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/email-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Location</div>
        <div class="text-icon">Numéro 139, 
Avenue de l’enseignement, Commune de KASA-VUBU Limeté,
10ème rue, numéro 334, référence petit-boulevard
Kinshasa, RDC</div>
      </div>
    </div>
  </div>
</div>

                </div>

                <div class="col-12 col-md-6">
                    <div class="form-box">

                        <div class="form-box-topic">
                            Prenez Contact:
                        </div>

                        <div class="form-box-content">
                            <form action="" method="post">
                                <div class="mb-3">
                                    <label for="name" class="form-labe">VOTRE NOM</label>
                                    <input type="text" class="form-inp" id="name" name="name" required>
                                </div>
                                <div class="mb-3">
                                    <label for="name" class="form-labe">VOTRE-EMAIL</label>
                                    <input type="email" class="form-inp" id="email" name="email" required>
                                </div>
                                <div class="mb-3">
                                    <label for="name" class="form-labe">PHONE NUMBER</label>
                                    <input type="tel" class="form-inp" id="phone" name="phone" required>
                                </div>
                                <div class="mb-3">
                                    <label for="message" class="form-labe">Message</label>
                                    <textarea class="form-textarea-labe" id="message" name="message" rows="4" required></textarea>
                                </div>
                                <button type="submit" class="btn-submit">Soumettre</button>
                            </form>
                        </div>

                    </div>
                </div>



            </div>
        </div>

        <div class="container" style="margin-top: 100px;">
            
            <div class="row">
                <div class="col-12 col-md-5"> 

                    <div class="contact-topic-box">
                        <div class="topicstyle-1"><b>Question fréquemment posée</b></div>
                        <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
                    </div>

                    <p class="contact-paragraph">
                  Vous avez d'autres questions ? N'hésitez pas à nous contacter pour plus d'informations.
                </p>

                </div>

                

                <div class="col-12 col-md-7"> 

                    <div class="container my-4">
  <div class="accordion" id="faqAccordion">
    <!-- FAQ Item 1 -->
    <div class="accordion-item border-0">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="false" aria-controls="faq1">
          <span>What is your return policy?</span>
          <span class="ms-auto arrow-icon">
            <!-- Down Arrow SVG -->
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq1" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p>You can return items within 30 days of purchase.</p>
          <p>Make sure the item is in original condition.</p>
        </div>
      </div>
    </div>

    <!-- FAQ Item 2 -->
    <div class="accordion-item border-0">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
          <span>How long does shipping take?</span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p>Standard shipping takes 3–5 business days.</p>
          <p>Express options are available at checkout.</p>
        </div>
      </div>
    </div>
  </div>
</div>
                    
                </div>

        </div>

    </div>

    <div class="container-fluid p-0">
    <div class="video-background">
        <video autoplay muted loop playsinline>
            <source src="<?= BASE_URL ?>/assets/video/waving-flag-1.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <div class="centered-content">
            <div class="centered-box">
                <h1 class="topic"><b>STATUT DE L'ACP</b></h1>
                <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
                <p>This is centered over a looping video background.</p>

                <img src="<?= BASE_URL ?>/assets/img/signed.png" class="signed" alt="">
            </div>
        </div>
    </div>
</div>

    <?php include 'includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</main>