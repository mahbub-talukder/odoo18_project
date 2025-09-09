<?php
$page = 'contact';          // used to load home.css
$title = 'Contactez-nous';
include 'includes/header.php';
?>

<main style="">
    <div id="successPopup" class="success-popup">
        <span class="close-popup">&times;</span>
        <p>Message envoyé avec succès!</p>
    </div>

    <div style="height: 160px;"></div>

    <div>

        <div class="container">
            <div class="row">
                <div class="col-12 col-md-6">
                
                    <div class="contact-topic-box">
                        <div class="d-inline-block">
                          <h3 class="contact-topic d-inline-block" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000"><b>Contactez-nous</b></h3>
                        <div class="line-something my-3" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
                        </div>
                    </div>

                    <p class="contact-paragraph" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">Que vous ayez des questions sur nos initiatives, besoin de soutien, ou souhaitiez partager vos commentaires, notre équipe dédiée est là pour vous assister à chaque étape.</p>

                    <div class="contact-info container" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
  <div class="row">
    <!-- Email -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/email-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Email</div>
        <div class="text-icon">media@acp.org.cd</div>
      </div>
    </div>

    <!-- Website -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/website-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Website</div>
        <div class="text-icon">www.acp.org.cd</div>
      </div>
    </div>

    <!-- Phone -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <span class=" icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/phone-icon.png" class="icon-img" alt=""></span>
      <div>
        <div class="fw-semibold">Téléphone</div>
        <div class="text-icon">+243 819 797 978</div>
      </div>
    </div>

    <!-- Location -->
    <div class="col-6 d-flex align-items-start gap-2 mb-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <span class="icon-placeholder mt-1"><img src="<?= BASE_URL ?>/assets/img/location-icon.png" class="icon-img" alt=""></span>
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

                <div class="col-12 col-md-6" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
                    <div class="form-box">

                        <div class="form-box-topic">
                            Prenez Contact:
                        </div>

                        <div class="form-box-content">
                            <form id="contactForm" action="" method="post">
                                <div class="mb-3">
                                    <label for="name" class="form-labe">Votre Nom</label>
                                    <input type="text" class="form-inp" id="name" name="name" required>
                                    <div class="error-message" id="name_error"></div>
                                </div>
                                <div class="mb-3">
                                    <label for="email" class="form-labe">Votre Email</label>
                                    <input type="email" class="form-inp" id="email" name="email" required>
                                    <div class="error-message" id="email_error"></div>
                                </div>
                                <div class="mb-3">
                                    <label for="phone" class="form-labe">Votre Téléphone</label>
                                    <input type="tel" class="form-inp" id="phone" name="phone" required>
                                    <div class="error-message" id="phone_error"></div>
                                </div>
                                <div class="mb-3">
                                    <label for="message" class="form-labe">Votre Message</label>
                                    <textarea class="form-textarea-labe" id="message" name="message" rows="4" required></textarea>
                                    <div class="error-message" id="message_error"></div>
                                </div>
                                <button type="submit" class="btn-submit" id="submitBtn"><b>Soumettre</b></button>
                            </form>
                        </div>

                    </div>
                </div>



            </div>
        </div>

        <div class="container" style="margin-top: 100px;">
            
            <div class="row">
                <div class="col-12 col-md-5" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000"> 

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

                

                <div class="col-12 col-md-7" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000"> 

                    <div class="container my-4">
  <div class="accordion" id="faqAccordion">
    <!-- FAQ Item 1 -->
    <div class="accordion-item border-0">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="false" aria-controls="faq1">
          <span>Qu'est-ce que l'adhésion Premium de l'ACP et comment fonctionne-t-elle ?</span>
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
          <p>L'adhésion Premium ACP—également connue sous le nom d'Ambassadeur ACP—est votre porte d'entrée vers un engagement plus profond avec le parti. En vous inscrivant via notre nouveau Système d'adhésion numérique (DMS), vous devenez officiellement partie prenante de notre mouvement croissant et accédez à des avantages exclusifs. Une fois inscrits, les membres recevront une carte de membre physique ACP, qui offre des privilèges spéciaux tels qu'un accès prioritaire aux événements ACP, des produits officiels du parti et d'autres opportunités réservées aux membres.</p>
          
        </div>
      </div>
    </div>

    <!-- FAQ Item 2 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
          <span>Comment puis-je rester informé des nouvelles et des activités de l'ACP ?</span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p>Vous pouvez nous suivre sur les réseaux sociaux (Facebook, Instagram, X, TikTok et YouTube) ou visiter régulièrement notre site web pour les dernières mises à jour, annonces d'événements et analyses politiques. Nous relançons nos plateformes en ligne pour mieux vous servir et vous garder plus connecté à notre mouvement.</p>
          
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
               <div class="d-inline-block" >
                 <h1 class="topic d-inline-block" data-aos="zoom-in" data-aos-delay="500" data-aos-duration="1000"><b>STATUT DE L'ACP</b></h1>
                <div class="line-something my-3">
        <div class="line-blue"></div>
        <div class="line-brown"></div>
        <div class="line-yellow"></div>
    </div>
               </div>
                <p>This is centered over a looping video background.</p>

                

                  <div class="container my-4">
  <div class="border rounded p-3" style="height: 500px; overflow: hidden;">
    <iframe 
      src="<?= BASE_URL ?>/assets/docs/statut-de-lacp.pdf" 
      width="100%" 
      height="100%" 
      style="border: none;">
    </iframe>
  </div>
</div>



            </div>
        </div>
    </div>
</div>

    <?php include 'includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        const successPopup = document.getElementById('successPopup');
        const closePopup = document.querySelector('.close-popup');

        closePopup.addEventListener('click', () => {
            successPopup.classList.remove('show');
        });

        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault();
            document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
            const formData = new FormData(this);
            
            fetch('<?= BASE_URL ?>/process_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    successPopup.classList.add('show');
                    this.reset();
                    setTimeout(() => {
                        successPopup.classList.remove('show');
                    }, 3000);
                } else if (data.errors) {
                    Object.keys(data.errors).forEach(field => {
                        const errorDiv = document.getElementById(`${field}_error`);
                        if (errorDiv) {
                            errorDiv.textContent = data.errors[field];
                        }
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>

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