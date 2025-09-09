<?php
$page = 'ligues-des-femmes';          // used to load home.css
$title = 'Ligues Des Femmes';
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
    ['name' => 'OLANGI', 'surname' => 'Ketsia', 'position' => 'Présidente', 'picture' => "/assets/img/ketsiaolangi.jpeg"],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
    ['name' => 'Nom', 'surname' => 'Post Nom', 'position' => 'Grade', 'picture' => null],
];
?>

<main>

    <div style="height: 160px;"></div>
	
	<div class="container parent-1 min-vh-100">
    <div class="w-100 centered-box"><img src="<?= BASE_URL ?>/assets/img/yello-blue-people.png" alt="Left Image" class=""></div>
    <div class="w-100 centered-box">
		<h1 class="topic-h"> Les femmes de l’A<span style="color:#8b0807;">C</span><span style="color:#f5d917;">P</span> </h1>
	</div>
    <div class="w-100 centered-box">
	
		<div class="d-inline-block">
              <h3 class="color-black" ><b>Les Forces Vives Féminines de l'ACP</b></h3>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>
	
	</div>
    <div class="w-100 centered-box text-center ubuntu-font">
	 <p class="paragraph-1">
		  Découvrez les femmes inspirantes de l'Alliance des Congolais Progressistes (ACP), qui sont la force de nos actions. Leur sagesse et détermination visent un Congo plus juste. Leurs profils illustrent l'engagement et la diversité des talents de notre mouvement. 
		</p>
	</div>
  </div>
  
  
  <div>

	<div class="container">
  <div class="">
    <div class="hero-inner">
      <!-- Background Image -->
      <img src="<?= BASE_URL ?>/assets/img/back-11.png" alt="Background" class="hero-image">

      <!-- Overlaid Content on Right -->
      <div class="row hero-content h-100">
        <div class="col-12 col-md-6 ms-auto h-100">
          <div class="content-box">

            <div class="space1"></div>

            <div class="d-inline-block">
              <h2 class="topicstyle-1" style="font-family: Allan;"><b>Vision de ligue des Femmes</b></h2>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>

            <div class="space2"></div>

            <p class="paragraph-3" style="font-size:18px;font-family: Allan;">
              La Ligue des Femmes de l'ACP vise à promouvoir l'égalité des genres et à renforcer le rôle des femmes dans la vie politique et dans la société. Nous aspirons à une représentation équitable des femmes à tous les niveaux de décision, du parti jusqu'aux instances gouvernementales. Nous nous engageons à soutenir et à autonomiser les femmes, en leur offrant les outils nécessaires pour exercer pleinement leurs droits et leur potentiel.
            </p>
            <p class="paragraph-3" style="font-size:18px;font-family: Allan;">
              Notre action se concentre sur la formation politique et le leadership féminin. Nous offrons des ateliers, des formations et des programmes de mentorat pour développer les compétences des femmes en matière de communication, de négociation et de prise de parole en public. Nous encourageons les femmes à prendre des responsabilités au sein du parti et à se présenter à des postes électifs.
            </p>
            <p class="paragraph-3" style="font-size:18px;font-family: Allan;">
              Enfin, nous nous engageons à défendre les droits des femmes et à promouvoir leurs intérêts. Nous luttons contre toutes les formes de discrimination et d'inégalité, en plaidant pour des politiques publiques qui favorisent l'égalité des chances et l'inclusion des femmes dans tous les domaines de la vie sociale et économique.
            </p>

            <div class="space3"></div>

            <!--<img src="<?= BASE_URL ?>/assets/img/people-in-blue-standing.png" class="position-absolute bottom-0 start-50 translate-middle-x" alt="Image"> -->

          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</div>

<div class="container parent-1 min-vh-100 d-flex align-items-center">


	<div class="row w-100 d-flex align-items-center">
    <div class="col-12 col-md-4 mb-3">
      <div class="p-3 text-black text-center">
	  
		<div class="d-inline-block">
              <h2 class="topicstyle-2 ubuntu-font"><b>NOTRE OBJECTIF</b></h2>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>
	  
	  </div>
    </div>
    <div class="col-12 col-md-4 mb-3">
      <div class="p-3 text-black d-flex justify-content-center"><img src="<?= BASE_URL ?>/assets/img/femmes-center-picture.png" class="vision-picture" alt=""></div>
    </div>
    <div class="col-12 col-md-4" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000"> 

                    <div class="container my-4">
  <div class="accordion" id="faqAccordion">
    <!-- FAQ Item 1 -->
    <div class="accordion-item border-0">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="false" aria-controls="faq1">
          <span>Promotion de l'égalité des genres </span>
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
          <p align="justify">La Ligue des femmes de l'ACP a pour ambition centrale de garantir une représentation équitable des femmes dans les sphères de décision, aussi bien au sein du parti politique qu'aux niveaux gouvernementaux.<br> <br>Il ne s'agit pas seulement d'une question de nombre, mais d'une volonté profonde d'intégrer les perspectives et les expériences féminines dans l'élaboration des politiques publiques. <br><br>La Ligue des femmes s'engage ainsi à promouvoir une véritable égalité des chances et à faire entendre la voix des femmes dans les processus décisionnels.</p>
          
        </div>
      </div>
    </div>

    <!-- FAQ Item 2 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
          <span>Autonomisation des femmes </span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify">Cet engagement envers les femmes se traduit par un soutien concret et multiforme, axé sur l'autonomisation et l'épanouissement personnel et professionnel. Au-delà des formations, elle met en place des programmes de mentorat individualisés, permettant aux femmes de bénéficier d'un accompagnement personnalisé de la part de femmes accomplies dans leurs domaines respectifs.<br><br> Ces mentorats offrent un soutien précieux pour surmonter les obstacles spécifiques rencontrés par les femmes, que ce soit dans le monde professionnel ou dans la vie personnelle. L'objectif est de créer un réseau de soutien solide et durable, où les femmes peuvent s'entraider, partager leurs expériences et s'encourager mutuellement à atteindre leur plein potentiel.<br><br> Les formations dispensées sont variées et conçues pour répondre aux besoins spécifiques des femmes, couvrant des domaines tels que le leadership, la gestion de projet, la communication, l'entrepreneuriat et le développement personnel. L'accent est mis sur le renforcement de la confiance en soi et l'acquisition d'outils pratiques pour une participation plus efficace à la vie publique et privée. <br><br>L'objectif ultime est de permettre aux femmes d'exercer pleinement leurs droits, de réaliser leurs ambitions et de contribuer pleinement à la société.<br>
          </p>
          
        </div>
      </div>
    </div>
    
    <!-- FAQ Item 3 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" aria-expanded="false" aria-controls="faq3">
          <span>Lutte contre la discrimination </span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify"> L'engagement de la Ligue des femmes de l'ACP va au-delà de la simple promotion de l'égalité des chances. Elle s'engage résolument dans la lutte contre toutes les formes de discrimination et de violence à l'égard des femmes, qu'elles soient d'ordre physique, psychologique, économique ou sexuel. <br><br>Cette lutte passe par une sensibilisation accrue de la population, la dénonciation des actes de violence et de discrimination, et un plaidoyer constant auprès des pouvoirs publics pour l'adoption de lois et de politiques publiques qui protègent les femmes et les filles. <br><br>L'objectif est de créer un environnement sûr et respectueux, où les femmes peuvent vivre pleinement leur vie, sans crainte ni menace.<br>
          </p>
          
        </div>
      </div>
    </div>
    
    <!-- FAQ Item 4 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" aria-expanded="false" aria-controls="faq4">
          <span>Encouragement à la participation politique </span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify"> La Ligue des femmes de l'ACP ne se contente pas d'encourager la participation des femmes à la politique ; elle met en place des stratégies concrètes pour les aider à s'engager activement et à prendre des responsabilités. <br><br>Cela passe par des programmes de formation politique et de leadership, conçus pour outiller les femmes et leur donner les moyens de s'exprimer, de négocier et de diriger. Des ateliers pratiques sur la communication politique, la gestion de campagne et la mobilisation citoyenne sont organisés régulièrement. <br><br>La Ligue offre également un accompagnement personnalisé aux femmes qui souhaitent se présenter à des postes électifs, en les aidant à élaborer leur programme, à constituer leur équipe et à mener une campagne efficace. Elle met à leur disposition un réseau de soutien et de mentorat, composé de femmes expérimentées qui partagent leurs connaissances et leur expérience.<br><br> L'objectif est de créer un environnement favorable à l'épanouissement des femmes en politique, en leur donnant les moyens de réussir et de faire entendre leur voix. Au-delà de la simple incitation, la Ligue des femmes de l'ACP offre un soutien concret et un accompagnement personnalisé pour permettre aux femmes de s'engager pleinement dans la vie politique et d'occuper les postes de décision qui leur reviennent de droit.
          </p>
          
        </div>
      </div>
    </div>
    
    <!-- FAQ Item 5 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq5" aria-expanded="false" aria-controls="faq5">
          <span>Développement de l'entrepreneuriat féminin  </span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq5" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify">  La Ligue des femmes de l'ACP s'engage activement dans le développement économique des femmes, convaincue que l'indépendance financière est un pilier fondamental de leur émancipation politique. Elle considère que l'autonomisation économique est intrinsèquement liée à l'autonomisation politique. Une femme financièrement indépendante est mieux à même de prendre des décisions libres, de s'engager pleinement dans la vie politique sans dépendre de pressions ou de contraintes financières, et de représenter efficacement les intérêts de sa communauté.<br><br> C'est pourquoi la Ligue met en place des programmes concrets pour soutenir les initiatives entrepreneuriales des femmes, en leur offrant des formations, des conseils, un accès au financement et un réseau de soutien. Ces programmes couvrent un large éventail de domaines, de la création d'entreprise à la gestion financière, en passant par le marketing et le développement commercial.<br><br> L'objectif est de créer un écosystème favorable à l'épanouissement de l'entrepreneuriat féminin, contribuant ainsi à une plus grande égalité des chances et à une participation politique plus significative des femmes.
          </p>
          
        </div>
      </div>
    </div>

  </div>
</div>
                    
                </div>
  </div>

</div>

<?php
$articles = [
  ['img' => 'femmes1.jpeg', 'title' => 'Title'],
  ['img' => 'femmes2.jpeg', 'title' => 'Title'],
  ['img' => 'femmes3.jpeg', 'title' => 'Title'],
  ['img' => 'femmes4.jpeg', 'title' => 'Title'],
  ['img' => 'femmes5.jpeg', 'title' => 'Title'],
  ['img' => 'femmes6.jpeg', 'title' => 'Title'],
  ['img' => 'femmes7.jpeg', 'title' => 'Title'],
    ['img' => 'femmes8.jpeg', 'title' => 'Title']
];
?>
<div class="container" data-aos="zoom-in" data-aos-delay="1000">
    <div class="row">
        <?php foreach ($articles as $article): ?>
            <div class="col-md-3">
                <div class="card">
                  <img src="<?= BASE_URL ?>/assets/img/<?= $article['img'] ?>" alt="<?= $article['title'] ?>">
                  <!--<h3 class="card-title"><?= $article['title'] ?></h3>-->
                </div>
            </div>
          <?php endforeach; ?>
    </div>
  
</div>

<div class="fifth-parent">

        
        
            <div class="container executive-team-parent">
                <div class="executive-team d-flex align-items-center justify-content-center">

                    <div class="topic-box">
                        <h2 class="topicstyle-1 text-center">Le Comité Exécutif de la ligue des Femmes de l'A<span style="color:#8b0807;">C</span><span style="color:#f5d917;">P</span></h2>
                        <p class="text-center">Découvrez les femmes dévouées qui dirigent l'Alliance des Congolais Progressistes (ACP). 
Ce comité exécutif est à l'avant-garde de nos initiatives, stimulant le progrès et plaidant pour l'amélioration de notre communauté. Chaque membre apporte une expertise inestimable et une passion pour créer un changement positif.</p>
                
                    </div>

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
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
	
	
	
</main>