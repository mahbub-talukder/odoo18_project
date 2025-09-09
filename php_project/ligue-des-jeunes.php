<?php
$page = 'ligue-des-jeunes';          // used to load home.css
$title = 'Ligue Des Jeunes';
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
    ['name' => 'MUPATA', 'surname' => 'Moïse', 'position' => 'Président', 'picture' => "/assets/img/mupatavrai.jpeg"],
    ['name' => 'MODISI', 'surname' => 'ROMEO', 'position' => 'Vice Président', 'picture' => "/assets/img/romeomudiso.jpeg"],
    ['name' => 'BADIBANGA', 'surname' => 'Suzy', 'position' => 'Vice Présidente', 'picture' => null],
    ['name' => 'Muini', 'surname' => 'Bertille', 'position' => 'Vice Présidente', 'picture' => null],
];
?>

<main>

    <div style="height: 160px;"></div>
	
	<div class="container parent-1 min-vh-100">
    <div class="w-100 centered-box" data-aos="zoom-in" data-aos-delay="1000"><img src="<?= BASE_URL ?>/assets/img/liguejeunes.jpeg" alt="Left Image" class=""></div>
    <div class="w-100 centered-box" data-aos="zoom-in" data-aos-delay="1000">
		<h1 class="topic-h"> La ligue des jeunes de l’A<span style="color:#8b0807;">C</span><span style="color:#f5d917;">P</span> </h1>
	</div>
    <div class="w-100 centered-box" data-aos="zoom-in" data-aos-delay="1000">
	
		<div class="d-inline-block" data-aos="zoom-in" data-aos-delay="1000">
              <h3 class="color-black" ><b>La Dynamique Jeunesse de l'ACP</b></h3>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>
	
	</div>
    <div class="w-100 centered-box text-center ubuntu-font">
	 <p class="paragraph-1">
		  Nous sommes la force vive et l'avenir de l'ACP. La Ligue des Jeunes rassemble des jeunes engagés, prêts à bâtir un Congo meilleur.
		</p>
	</div>
  </div>
  
  
  <div>

	<div class="container">
  <div class="">
    <div class="hero-inner">
      <!-- Background Image -->
      <img src="<?= BASE_URL ?>/assets/img/back-12.png" alt="Background" class="hero-image" data-aos="fade-up" data-aos-delay="1000">

      <!-- Overlaid Content on Right -->
      <div class="row hero-content h-100" data-aos="fade-down" data-aos-delay="500">
        <div class="col-12 col-md-6 ms-auto h-100">
          <div class="content-box">

            <!--<div class="space1"></div>-->

            <div class="d-inline-block">
              <h2 class="topicstyle-1" style="font-family: Allan;"><b>Vision de la ligue des Jeunes</b></h2>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>

            <!--<div class="space2"></div>-->

            <p class="paragraph-3" align="justify" style="font-size:18px;font-family: Allan;">
              <!--Renforcer la connexion entre le parti et les jeunes, dans un contexte où la jeunesse congolaise doit affronter des défis politiques, sociaux et économiques complexes.-->
              La Ligue des Jeunes de l'Alliance des Congolais Progressistes (ACP) ambitionne d'être le fer de lance du renouveau politique et du progrès social en RDC. Elle incarne une jeunesse congolaise responsable, mobilisée et influente, participant activement à la construction d'un Etat moderne, équitable et souverain, fidèle aux valeurs de l'ACP. Son objectif est de former une nouvelle génération de leaders politiques compétents, intègres et patriotes.
			</p>
			
			<p class="paragraph-3" align="justify" style="font-size:18px;font-family: Allan;">
              La Ligue des jeunes vise à être un incubateur de leadership, offrant aux jeunes l'opportunité de s'informer, se former, s'exprimer et agir en toute conscience citoyenne. Elle combat l'exclusion des jeunes des processus décisionnels et promeut leur participation réelle à la gouvernance. L'éducation politique, l'engagement civique et l'entrepreneuriat social sont au cœur de son action, visant à autonomiser les jeunes et à leur permettre de contribuer activement au développement du pays.
			</p>
			<p class="paragraph-3" align="justify" style="font-size:18px;font-family: Allan;">
              La vision de la Ligue des jeunes s'inscrit dans une perspective panafricaine et progressiste. Elle ambitionne de faire de la jeunesse congolaise un acteur clé du développement du continent, tout en renforçant l'unité nationale et en valorisant l'identité congolaise. Elle rêve d'un Congo où chaque jeune, où qu'il soit, peut comprendre les enjeux de sa société, participer à sa gouvernance et proposer des solutions innovantes.
			</p>
			<p class="" align="center" style="font-size:18px;font-family: Allan;">
              ACP VIVA !!!
			</p>
			
			
            <div class="space3"></div>

            <!--<img src="<?= BASE_URL ?>/assets/img/raised-hands-colors.png" class="position-absolute bottom-0 start-50 translate-middle-x" alt="Image"> -->

          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</div>

<!-- test -->
<div class="container parent-1 min-vh-100 d-flex align-items-center">


	<div class="row w-100 d-flex align-items-center">
        <div class="col-12 col-md-5 mb-3">
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
        <div class="col-12 col-md-7" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000"> 

                    <div class="container my-4">
  <div class="accordion" id="faqAccordion">
    <!-- FAQ Item 1 -->
    <div class="accordion-item border-0">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="false" aria-controls="faq1">
          <span>Mobilisation et Recrutement</span>
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
          <p align="justify">La Ligue des Jeunes de l’ACP se donne pour mission première de renforcer sa base militante en recrutant activement une nouvelle génération de jeunes engagés. Consciente que la vitalité d’un mouvement politique repose sur la capacité à renouveler ses forces, la Ligue entend attirer des jeunes hommes et femmes issus de toutes les couches sociales, sensibilisés aux défis contemporains de la République Démocratique du Congo, et désireux de contribuer activement à son progrès. Le recrutement ne se limite pas à une simple inscription administrative, mais s’inscrit dans une logique de conviction : il s’agit de faire adhérer la jeunesse aux idéaux fondateurs de l’ACP, notamment le progrès, la justice sociale, la bonne gouvernance et la souveraineté nationale.</p>
          <p align="justify">Pour stimuler cette dynamique, la Ligue prévoit l’organisation régulière d’événements fédérateurs, tels que des conférences politiques, des ateliers de formation, des meetings populaires, mais aussi des initiatives à forte valeur citoyenne, telles que des campagnes de sensibilisation, des collectes de fonds solidaires ou encore des actions communautaires. Ces activités ont un double objectif : créer un espace de participation et de dialogue pour les jeunes, tout en ancrant l’image de l’ACP dans un discours de proximité, de modernité et d’utilité sociale. À travers ces actions, la Ligue veut également bâtir un réseau structuré et actif de jeunes militants à travers les différentes provinces du pays, afin d’assurer une présence territoriale durable et cohérente.</p>
          
        </div>
      </div>
    </div>

    <!-- FAQ Item 2 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
          <span>Formation et Éducation Politique</span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify">Au-delà du recrutement, la Ligue des Jeunes de l’ACP ambitionne de transformer ses membres en véritables acteurs du changement par une politique de formation continue et d’éducation politique. Consciente que l’engagement ne peut être durable sans compréhension des enjeux, elle met en place des modules de formation visant à familiariser les jeunes avec les valeurs et les programmes du parti, les grandes problématiques nationales et internationales, ainsi que les mécanismes du jeu politique. Ces sessions aborderont notamment les techniques de campagne électorale, les stratégies de mobilisation, le militantisme éthique, mais aussi la prise de parole en public et la communication politique.<br>
              Il s’agit également de renforcer les compétences pratiques des jeunes en matière d’organisation d’événements, de gestion de projets, de leadership local, et de travail en équipe. La Ligue entend ainsi former des jeunes capables d’agir efficacement sur le terrain et d’assumer des responsabilités politiques à court ou moyen terme. Par ailleurs, elle encourage la réflexion critique à travers l’organisation de débats publics, de cafés politiques ou de simulations parlementaires, offrant ainsi un espace où les jeunes peuvent confronter leurs idées, se forger une opinion politique éclairée, et exercer leur citoyenneté de manière active. L’éducation à la citoyenneté inclura également des thèmes d’intérêt général tels que les droits humains, l’environnement, l’économie nationale ou encore la lutte contre les inégalités, permettant aux jeunes de développer une conscience politique complète et engagée.
          </p>
          
        </div>
      </div>
    </div>
    
    <!-- FAQ Item 3 -->
    <div class="accordion-item border-0" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" aria-expanded="false" aria-controls="faq3">
          <span>Action Politique et Engagement Civique</span>
          <span class="ms-auto arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="down-arrow" viewBox="0 0 16 16">
              <path d="M1.5 5.5l6 6 6-6" stroke="black" stroke-width="2" fill="none"/>
            </svg>
          </span>
        </button>
      </h2>
      <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
        <div class="accordion-body">
          <p align="justify">La Ligue des Jeunes de l’ACP ne se limite pas à un rôle d’accompagnement ou de soutien. Elle se positionne comme une force d’action politique autonome et proactive, en prise directe avec les réalités de terrain. Lors des échéances électorales, elle mobilise ses membres pour soutenir les candidats du parti à travers des campagnes de proximité, le porte-à-porte, la distribution de tracts, l’animation des réseaux sociaux, et l’organisation de rassemblements publics. Elle joue un rôle clé dans la dynamique électorale de l’ACP, en constituant un vivier de militants formés, motivés et visibles.<br>
              Mais l’engagement de la Ligue va bien au-delà du temps électoral. Tout au long de l’année, elle mène des actions citoyennes concrètes : campagnes de nettoyage dans les quartiers défavorisés, opérations de reboisement, collectes de denrées alimentaires, sensibilisation à la santé publique ou à l’éducation. Ces initiatives traduisent la volonté de la Ligue d’ancrer l’engagement politique dans le quotidien des Congolais, en apportant des solutions tangibles aux défis locaux. En parallèle, elle s’attache à représenter les intérêts de la jeunesse auprès des autorités et des institutions, en exerçant une pression constructive sur les élus pour que les préoccupations des jeunes soient prises en compte dans les politiques publiques. Elle se positionne ainsi comme un interlocuteur légitime dans l’élaboration des stratégies de développement local et national.
          </p>
          
        </div>
      </div>
    </div>

  </div>
</div>
                    
                </div>
      </div>

</div>
<!-- end test -->

<div>

<div class="container mt-5">
  <div class="container">
    <div class="hero-inner">
      <!-- Background Image -->
      <img src="<?= BASE_URL ?>/assets/img/liguej2.jpeg" alt="Background" class="hero-image">

      <!-- Overlaid Content on Right -->
      <div class="row hero-content">
        <div class="col-12 col-md-6 ms-auto">
          <div class="content-box" data-aos="fade-up" data-aos-delay="1500">

            <div class="d-inline-block">
              <h2 class="topicstyle-1"><b>Nos Programmes</b></h2>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>

            <p class="paragraph-3">
                <ul>
                    <li>Chaque Samedi à 15h les Comités nationaux se réunit autour de leur président</li>
                    <li>Chaque Vendredi à 15h les comités inter-fédéraux se réunit autour de leur président inter-fédéraux</li>
                    <li>Chaque Jeudi à 15h, les comités fédéraux se réunit autour de leur présidents fédéraux</li>
                    <li>Chaque mercredi à 15h, les comités communaux se réunit autour de leur présidents communaux</li>
                    <li>Chaque mardi à 15h, les comités sectionnaires se réunit autour de leur présidents sectionnaires</li>
                </ul>
			</p>
			 <p class="paragraph-3">A cet effet un rapport d’activité est dressé à l’intention du Président National de la ligue des jeunes pour exploitation.</p>
			 
			 <p>Contact : <b>+243 999 034 990</b></p>

            <!--<img src="<?= BASE_URL ?>/assets/img/raised-hands-colors.png" class="position-absolute bottom-0 start-50 translate-middle-x" alt="Image">-->

          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</div>

<?php
$articles = [
  ['img' => 'jeunes1.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes5.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes2.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes6.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes3.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes7.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes4.jpeg', 'title' => 'Title'],
    ['img' => 'jeunes8.jpeg', 'title' => 'Title'],
    ['img' => 'jeunes9.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes10.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes11.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes12.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes13.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes14.jpeg', 'title' => 'Title'],
  ['img' => 'jeunes15.jpeg', 'title' => 'Title'],
    ['img' => 'jeunes16.jpeg', 'title' => 'Title']
];
?>
<div class="container mt-5 mb-5" data-aos="fade-up" data-aos-delay="1500">
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
                        <h2 class="topicstyle-1 text-center">Le Comité Exécutif de la ligue des Jeunes de l'A<span style="color:#8b0807;">C</span><span style="color:#f5d917;">P</span></h2>
                        <p class="text-center">Découvrez la jeunesse engagée qui anime l'Alliance des Congolais Progressistes (ACP). Ce comité exécutif représente la nouvelle génération, pleine d'énergie et de détermination pour bâtir un avenir meilleur pour tous.
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