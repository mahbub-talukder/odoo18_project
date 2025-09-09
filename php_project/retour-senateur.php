<?php
$page = 'retour-senateur';          // used to load home.css
$title = 'Retour de Gentiny';
$metatitle = 'Retour de Gentiny Ngobila à Kinshasa';
$metaimage = 'arrive.jpeg';
$metaurl = 'retour-senateur.php';
$metadesc = "Kinshasa, le 4 janvier 2025 – L’ancien gouverneur de Kinshasa, Gentiny Ngobila Mbaka, est de retour à Kinshasa après un séjour à l’étranger pour raisons de santé.";
include 'includes/header.php';
?>

<main style="">
	<div style="height: 160px;"></div>
	
	<div class="container d-flex justify-content-center align-items-center" style="height: 200px;">
  <h1 class="text-center" style="color: #0400b7;"><b>Retour de Gentiny Ngobila à Kinshasa – Un engagement renouvelé pour le développement de la ville</b></h1>
</div>

<div class="container my-4">
  <!-- First full-width row with left and right-aligned content -->
  <div class="d-flex justify-content-between w-100">
    <div class="ubuntu-font">Janvier, 2025</div>
    <div class="ubuntu-font">Par l'Administrateur</div>
  </div>

  <!-- Second empty div -->
  <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
</div>

<!--<p class="text-center container ">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac consectetur urna. Duis eget interdum ipsum.</p>-->

<div class="container-fluid p-0">
  <img src="<?= BASE_URL ?>/assets/img/arrive.jpeg" class="img-fluid w-100" alt="Full width image">
</div>

<p class="mb-5 mt-5 container ubuntu-font" style="color: #0400b7;"><b>Kinshasa, le 4 janvier 2025 – L’ancien gouverneur de Kinshasa, Gentiny Ngobila Mbaka, est de retour à Kinshasa après un séjour à l’étranger pour raisons de santé. Son arrivée a été marquée par un accueil chaleureux de la part de ses partisans, témoignant de son attachement profond à la ville et à sa population.</b></p>

<div class="container d-flex align-items-center" style="height: 10px;">
  <!--<h2 class="text-start" style="color: #0400b7;"><b>NEWSPAPER</b></h2>-->
</div>

<div class="container my-4">
  <div class="row">
    <div class="col-md-6 mb-3" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <div class="">
	  
		<!--<p class="ubuntu-font"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac consectetur urna. Duis eget interdum ipsum. Praesent quis maximus elit, non mattis neque. Nam consequat felis et lacus ultricies finibus. </p>
		
			<div>

				<h2 class="ubuntu-font" style="color: #febc11;"><b>Quote text can be place here.</b></h2>
			</div>-->
			<p class="ubuntu-font" align="justify">L’arrivée de Gentiny Ngobila à Kinshasa le 04 Janvier 2025, a été plus qu’un simple retour de vacances. Vêtu d’une veste bleue et d’une casquette noire, le leader de l’<b>ACP</b> (Alliance des Congolais Progressistes) a été accueilli par une foule immense et enthousiaste à l’aéroport de N’Djili. Des milliers de partisans ont salué leur champion, malgré les nombreuses cabales dont il a été victime durant son mandat de gouverneur.</p>
		
		<b>Popularité intacte</b>
		<p class="ubuntu-font" align="justify"> Malgré les accusations et les attaques, <b>Gentiny Ngobila</b> reste une figure politique majeure en RDC, particulièrement à Kinshasa. Sa popularité auprès des Kinois est indéniable. Son retour suscite un réel espoir, notamment concernant le bien-être de la population. </p>
		<?php
$articles = [
  ['img' => 'arrive1.jpeg', 'title' => 'Title'],
  ['img' => 'arrive2.jpeg', 'title' => 'Title']
];
?>
<div class="container">
    <div class="row">
        <?php foreach ($articles as $article): ?>
            <div class="col-md-6">
                <div class="card">
                  <img src="<?= BASE_URL ?>/assets/img/<?= $article['img'] ?>" alt="<?= $article['title'] ?>" height="150">
                  <!--<h3 class="card-title"><?= $article['title'] ?></h3>-->
                </div>
            </div>
          <?php endforeach; ?>
    </div>
  
</div>
	  
	  <b>Un soutien crucial pour Tshisekedi ?</b>
		<p class="ubuntu-font" align="justify"> Le retour de Gentiny Ngobila intervient dans un contexte politique tendu, marqué par le projet de révision constitutionnelle porté par le président Félix Tshisekedi. Fervent soutien du chef de l’État, Gentiny Ngobila est attendu pour apporter son poids politique à ce projet controversé, accusé par l’opposition de vouloir permettre à Tshisekedi de se maintenir au pouvoir au-delà de 2028.


 </p>

 
		
		
	  </div>
    </div>
    <div class="col-md-6 mb-3" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">
      
	  <div class="">
	      <p class="ubuntu-font" align="justify">L’arrivée de Gentiny Ngobila pourrait redynamiser la majorité présidentielle, l’Union Sacrée, récemment secouée par des dissensions internes. Le président Tshisekedi lui-même a exprimé son mécontentement face à certains cadres de sa coalition. Le retour de Gentiny Ngobila et son influence pourraient donc jouer un rôle clé dans la restructuration de la majorité et le soutien au projet de révision constitutionnelle.</p>
	       <b>Un atout politique, mais des risques ?</b>
	      <p class="ubuntu-font" align="justify">
     Si le retour de Gentiny Ngobila est perçu comme un atout politique pour la majorité, il n’est pas sans risques. Ses démêlés passés avec la justice et les accusations dont il a fait l’objet pourraient être instrumentalisés par l’opposition. Le soutien de Gentiny Ngobila au projet de révision constitutionnelle sera scruté de près, devenant un enjeu majeur dans les mois à venir. Le prochain chapitre de sa carrière politique sera décisif, tant pour lui que pour l’avenir politique de la RDC.
 </p>
 		<?php
$articles = [
  ['img' => 'arrive3.jpeg', 'title' => 'Title'],
  ['img' => 'arrive4.jpeg', 'title' => 'Title']
];
?>
<div class="container">
    <div class="row mb-3">
        <?php foreach ($articles as $article): ?>
            <div class="col-md-6">
                <div class="card">
                  <img src="<?= BASE_URL ?>/assets/img/<?= $article['img'] ?>" alt="<?= $article['title'] ?>" height="150">
                  <!--<h3 class="card-title"><?= $article['title'] ?></h3>-->
                </div>
            </div>
          <?php endforeach; ?>
    </div>
  
</div>
 
	    <!--<b>Un futur prometteur pour Kinshasa :</b>
		<p align="justify"> Le retour de Gentiny Ngobila est un moment important pour la vie politique kinois. Son engagement, son expérience et sa détermination à servir la ville sont des atouts majeurs pour les années à venir. Nous avons confiance en son action pour une Kinshasa prospère et dynamique.</p>-->
		
		<!--<p class="ubuntu-font"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac consectetur urna. Duis eget interdum ipsum. Praesent quis maximus elit, non mattis neque. Nam consequat felis et lacus ultricies finibus.Vivamus ac ullamcorper dolor. Phasellus at dolor egestas, aliquet nulla eu </p>
	  
	  <p class="ubuntu-font"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac consectetur urna. Duis eget interdum ipsum. Praesent quis maximus elit, non mattis neque. Nam consequat felis et lacus ultricies finibus. </p>
		
		<p class="ubuntu-font"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac consectetur urna. Duis eget interdum ipsum. Praesent quis maximus elit, non mattis neque. Nam consequat felis et lacus ultricies finibus.Vivamus ac ullamcorper dolor. Phasellus at dolor egestas, aliquet nulla eu </p> -->
	  
	  </div>
	  
    </div>
    <!-- ShareThis BEGIN --><div class="sharethis-inline-reaction-buttons"></div><!-- ShareThis END -->
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