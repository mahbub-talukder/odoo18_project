<?php
$page = 'nos-realisations';          // used to load home.css
$title = 'nos-realisations';
$metatitle = 'Nos acquis';
$metaurl = 'nos-realisations.php';
$metadesc = "Découvrez nos réalisations et rejoignez le changement.";
include 'includes/header.php';

?>

<main>

	<div style="height: 160px;"></div>

 <div class="first-parent">
 
 <div class="text-center">
  
    <div class="w-100 centered-box">
		<h1 class="topic-h">Nos Réalisations</h1>
	</div>
    <div class="w-100 centered-box">
	
		<div class="d-inline-block">
              <h3 class="color-black" ><b>Découvrez nos réalisations et rejoignez le changement</b></h3>

              <div class="line-something my-3">
                <div class="line-blue"></div>
                <div class="line-brown"></div>
                <div class="line-yellow"></div>
              </div>
            </div>
	
	</div>
    <div class="w-100 centered-box text-center ubuntu-font">
	 <p class="paragraph-1">
		  Grâce à votre soutien, l’ACP transforme les communautés à travers des projets réels et durables. Ensemble, continuons à bâtir l’avenir de la RDC.
		</p>
	</div>
	
	</div>
</div>

<?php
$articles = [
  ['img' => '11.png', 'title' => 'Title'],
  ['img' => '12.png', 'title' => 'Title'],
  ['img' => '13.png', 'title' => 'Title'],
  ['img' => '14.png', 'title' => 'Title'],
  ['img' => '15.png', 'title' => 'Title'],
  ['img' => '16.png', 'title' => 'Title'],
  ['img' => '17.png', 'title' => 'Title'],
  ['img' => '18.png', 'title' => 'Title'],
  ['img' => '19.png', 'title' => 'Title']
];
?>

<div class="container">
    <!--Réalisation-->
    <div class="row text-center">
        <h2 class="ubuntu-font" style="color: #0400b7;"><b>I. Construction, Réhabilitation et Modernisation</b></h2>
        <!--Route Elengesa-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route Elengesa</b></h2>
            <p class="ubuntu-font">
                Longue de 6,2km, traversant les communes de Kalamu, Ngiri-Ngiri, Makala, Selembao, Bumbu et Mont-Ngafula ;</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Route Kikwit-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route Kikwit</b></h2>
            <p class="ubuntu-font">
                Longue de 5,3Km, traversant les communes de Limete, Lemba, Ngaba, Makala, Kalamu et Bumbu;</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Route Mombele-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route Mombele</b></h2>
            <p class="ubuntu-font">
                Longue de 2,7Km, traversant les communes de Limete et Lemba ;</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Route De la Paix-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route De la Paix</b></h2>
            <p class="ubuntu-font">
                Longue de 14Km, traversant les communes de Limete, Matete, Kisenso et Mont-Ngafula ;</p>
                <div class="row">
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix1.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix2.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix3.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix4.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix5.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix6.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix7.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix8.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/paix/paix9.jpeg" alt="">
                        </div>
                    </div>
                </div>
        </div>
        
        <!--Route Bongolo-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route Bongolo</b></h2>
            <p class="ubuntu-font">
                Reliant l’avenue Kasa-Vubu et le Rond-point Yolo Médical</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Pont moderne sur Bongolo-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Pont moderne sur Bongolo</b></h2>
            <p class="ubuntu-font">
                Avec la construction d’un canal à deux chaussées et une passerelle avec le parc Ngobila parallèle à la rivière Funa;
                </p>
                <div class="row">
                    <div class="col-md-12 mb-3 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/R2sTCVdotwc?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="Pont moderne sur Bongolo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        <!--Avenue Mongala-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Mongala</b></h2>
            <p class="ubuntu-font">
                Dans la communbe de la Gombe;</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Victoire-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Victoire</b></h2>
            <p class="ubuntu-font">
                Tronçon compris entre Rond-point Victoire
et l’avenue Ethiopie;</p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Makoma-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Makoma</b></h2>
            <p class="ubuntu-font">
                A Binza Ozone dans la commune de Ngaliema;
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Route CECOMAF-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route CECOMAF</b></h2>
            <p class="ubuntu-font">
                Longue de 15Km, traversant les communes de N’Djili, Kimbanseke et Mont-Ngafula pour déboucher sur la frontière avec la province du Kongo Central;
                </p>
                <div class="row">
                    <div class="col-md-12 mb-3 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/2SzH9zHQDrs?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="PONT LUBUDI ET ROUTE CECOMAF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <!--Avenue Libération-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Libération</b></h2>
            <p class="ubuntu-font">
                 Bétonnage sur 300 mètres entre l’avenue Landu et le marché Selembao;
                 </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Ngiri-Ngiri-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Ngiri-Ngiri</b></h2>
            <p class="ubuntu-font">
                 Tronçon compris entre Assossa et Libération;
                 </p>
                <div class="row">
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri1.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri2.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri3.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri4.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri5.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri6.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri7.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri8.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/ngiri-ngiri/ngiri9.jpeg" alt="">
                        </div>
                </div>
                
                </div>
        </div>
        
        <!--Avenue Birmanie-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Birmanie</b></h2>
            <p class="ubuntu-font">
                 Travaux en cours sur une longueur de 4,9Km, traversant les communes de Kasa-Vubu, Ngiri-Ngiri et Bumbu;
                 </p>
                <div class="row">
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie1.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie2.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie3.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie4.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie5.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie6.jpeg" alt="">
                        </div>
                </div>
                <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/birmanie/birmanie7.jpeg" alt="">
                        </div>
                </div>
        </div>
        
        <!--Pont Camps Luka -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Pont Camps Luka </b></h2>
            <p class="ubuntu-font">
                Sur la rivière Lubudi 
                </p>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/2SzH9zHQDrs?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="PONT LUBUDI ET ROUTE CECOMAF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <!--Route Landu -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route Landu </b></h2>
            <p class="ubuntu-font">
                De l’avenue Libération jusqu’au pont Lubudi ;
                </p>
                <div class="row">
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu1.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu2.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                        
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu3.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu4.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu5.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu6.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu7.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div></div>
                            <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/route-landu/landu8.jpeg" alt="">
                    	 
                          <!--<h3 class="card-title"></h3>-->
                        </div>
                            </div>
                </div>
        </div>
        
        <!--Routes Wangata, Usoke et Hôpital -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Routes Wangata, Usoke et Hôpital </b></h2>
            <p class="ubuntu-font">
                2,20 km ;
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Nguma -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Nguma </b></h2>
            <p class="ubuntu-font">
                Dans la commune de Ngaliema (Tronçon de Kintambo magasin – route de matadi)
                </p>
                <div class="row">
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma1.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma2.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma3.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma4.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma5.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma6.jpeg" alt="avenue nguma">
                        </div>
                    </div><div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma7.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/nguma/nguma8.jpeg" alt="avenue nguma">
                        </div>
                    </div>
                    
                </div>
        </div>
        
        <!--Boulevard Salongo-Mwana Wuta -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Boulevard Salongo-Mwana Wuta </b></h2>
            <p class="ubuntu-font">
                Dans la commune de Lemba (3,980km) ;
                </p>
                <div class="row">
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo1.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo2.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo3.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo4.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo5.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo6.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo7.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo8.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo9.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo10.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/salongo/salongo11.jpeg" alt="">
                        </div>
                    </div>
                    
                </div>
            
        </div>
        
        <!--Avenue Kasa-vubu -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Kasa-vubu </b></h2>
            <p class="ubuntu-font">
                Tronçon du Boulvard du 30 juin à la place Victoire ;
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
        <!--Boucle Matonge 1, Oshwe-Mpozo et permanence-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Boucle Matonge 1, Oshwe-Mpozo et permanence </b></h2>
            <p class="ubuntu-font">
                </p>
                <div class="row">
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/mponzo/mponzo1.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/mponzo/mponzo2.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/mponzo/mponzo3.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/mponzo/mponzo4.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/mponzo/mponzo5.jpeg" alt="">
                        </div>
                    </div>
                </div>
            
        </div>
        
        <!--Avenue de la Nation-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue de la Nation</b></h2>
            <p class="ubuntu-font">Dans la commune de la Gombe
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
        <!--Avenue Chrétien-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Chrétien</b></h2>
            <p class="ubuntu-font">Dans la commune de Kintambo
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
        <!--Marché central de Kinshasa-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Marché central de Kinshasa</b></h2>
            <p class="ubuntu-font">Avec une capacité de plus 80.000 places;
                </p>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/3rjn-S5erdc?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="Marché central" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando1.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando2.jpeg" alt="">
                        </div>
                            </div>
                        
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando3.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando4.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando5.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando6.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando7.jpeg" alt="">
                        </div></div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando8.jpeg" alt="">
                        </div>
                            </div>
                            <!--Suite--->
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando9.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando10.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando11.jpeg" alt="">
                        </div>
                            </div>
                        
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando13.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando14.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando15.jpeg" alt="">
                        </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/zando/zando16.jpeg" alt="">
                        </div></div>
                            
                </div>
            
        </div>
        
        <!--Marché central de Kinshasa-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Marché moderne Type-K.</b></h2>
            <p class="ubuntu-font">
                </p>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/O8Z3rtTciYo?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="Marché moderne Type-K" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
            
        </div>
        
    </div>
    <!--Des routes alimentées en éclairage public-->
    <div class="row text-center">
        <h2 class="ubuntu-font" style="color: #0400b7;"><b>II. Des routes alimentées en éclairage public</b></h2>
        <!--Avenue Kasavubu-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Kasa-Vubu</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Boulevard 30 juin-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Boulevard du 30 juin</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Boulevard Lumumba;-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Boulevard Lumumba;</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Avenue des Poids Lourds-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue des Poids Lourds</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Route By-pass-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Route By-pass</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Nguma;-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Nguma;</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        <!--Avenue Université-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Université</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Elengesa;-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Elengesa;</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Libération-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Libération</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Victoire-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Victoire</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3 yt-responsive">
            <iframe width="100%" src="https://www.youtube.com/embed/OiwSYYHRgKA?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="Des routes alimentées en éclairage public" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        
        <!--De la 1ère porte FIKIN jusqu’au Terminus via Super-Lemba-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>De la 1ère porte FIKIN jusqu’au Terminus via Super-Lemba</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue des Huileries-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue des Huileries</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Boulevard Kimbuta-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Boulevard Kimbuta</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Modjiba -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Modjiba </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue du Tourisme -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue du Tourisme </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Shaba -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Shaba </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Landu -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Landu </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <!--Avenue Enseignement -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Enseignement </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
        <!--Avenue Inga -->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Inga </b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
        <!--Avenue des Ecuries-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue des Ecuries </b></h2>
            <p class="ubuntu-font">
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        <!--Avenue Bangala-->
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Avenue Bangala </b></h2>
            <p class="ubuntu-font">
                </p>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
            
        </div>
        
    </div>
    <!--Aménagement et embellissement de la ville-->
    <div class="row text-center">
        <h2 class="ubuntu-font" style="color: #0400b7;"><b>III. Aménagement et embellissement de la ville</b></h2>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Partenariat avec l’entreprise OK Plast dans le cadre du
projet Kintoko pour la transformation et valorisation des
bouteilles plastiques</b></h2>
                <div class="row">
                    <div class="col-md-12 mb-3 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/KVmJHpqbFJw?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="OK PLAST ET ALBAYRAK" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Partenariat avec la société OK Clean pour la collecte et le recyclage des bouteilles plastiques</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Partenariat avec la société turque Albayrak pour la collecte et l’évacuation des déchets à Kinshasa</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Verdunisation des emprises du Boulevard Lumumba et
intégration de Fontaines et autres bancs</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Création des parcs d’attraction : place Wenge, parc Maman Marthe Kasalu Tshisekedi entre 3ème et 6ème rue Limete résidentiel, parc Wenze Hindou à Masina, parc Ngobila entre Bongolo-Victoire et parc super Lemba</b></h2>
                <div class="row">
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila1.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila2.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila3.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila4.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila5.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_ngobila/parc_ngobila6.jpeg" alt="parc ngobila">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_maman_marthe/parc_maman_marthe1.jpg" alt="parc maman marthe">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_maman_marthe/parc_maman_marthe2.jpg" alt="parc maman marthe">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_maman_marthe/parc_maman_marthe3.jpg" alt="parc maman marthe">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_maman_marthe/parc_maman_marthe4.jpg" alt="parc maman marthe">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/parc_maman_marthe/parc_maman_marthe5.jpg" alt="parc maman marthe">
                        </div>
                    </div>
                    <div class="col-md-4 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/rKGfkWmhXPY?rel=0?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="Parc Maman Marthe Kasalu Tshisekedi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                    <div class="col-md-4 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/2g_y9YGMmdY" title="EMBELISSEMENT SUPER LEMBA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                    <div class="col-md-4 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/1r0kZEogBKw?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="PARC WENGE A GOMBE AVANT PENDANT APRES" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Embellissement de la place de la Gare Centrale et décoration de la ville pour les festivités de Noël et de nouvel an</b></h2>
                <div class="row">
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue2.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue3.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue4.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue12.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue14.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue15.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue23.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue22.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue26.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue20.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue8.jpeg" alt="">
                        </div>
                    </div>
                    <div class="col-md-3">
                                <div class="card">
                          <img src="<?= BASE_URL ?>/assets/img/realisation-list/grande_roue/grande_roue21.jpeg" alt="">
                        </div>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction de la grande roue de 60 mètre à la place de la gare centrale.</b></h2>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/3H85zS1TaI8" title="AQUA   PARC   GRANDE ROUE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction du centre omnisport de Kalamu.</b></h2>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/euZQ20PPY-s" title="Centre Sportif Kalamu" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Embellissement de la place commercial Limeté 7ème</b></h2>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/GcXgMi2LwCs?list=PLvC4TBybDJjAfqRNqe6ODxPZo4KRyuV41" title="PARC LIMETE AVANT PENDANT APRES" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction du centre omnisport de Lemba salongo.</b></h2>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/YhxcGW6Goog" title="Centre Omnisport lemba salongo sud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Réhabilitation et embellissement du terrain de basket de la 7ème rue.</b></h2>
                <div class="row">
                    <div class="col-md-12 yt-responsive">
                        <iframe width="100%" src="https://www.youtube.com/embed/tojDKaFU6YU" title="Terrain de Basket Place Commercial 7eme rue Limete" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
        </div>
        
    </div>
    <!--Création-->
    <div class="row text-center">
        <h2 class="ubuntu-font" style="color: #0400b7;"><b>IV. Création</b></h2>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Régie de Gestion des Marchés de Kinshasa (REGEMK)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Direction Générale de Publicité Extérieure de Kinshasa(DGPEK)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Office de Contrôle de l’estampillage de Kinshasa (OCEKIN)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Coordination Kinshasa Bopeto</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Coordination pour la Promotion des Investissements et le Suivi des Réalisations des Projets (COPISREP)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Agence Provinciale pour le Développement du Numérique de Kinshasa (APDNK)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Brigade Anti-fraude de Kinshasa (BFKIN)</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Unité Spéciale pour la Protection de l’Environnement (USPE).</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
    </div>
    <!--Appui aux structures de santé-->
    <div class="row text-center">
        <h2 class="ubuntu-font" style="color: #0400b7;"><b>V. Appui aux structures de santé</b></h2>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Réhabilitation de la maternité de Kintambo et remise d'importants matériels et équipements</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction d'un funérarium moderne à l'hôpital de
Kintambo</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction d'un bâtiment moderne au Centre Mère et Enfant de Bumbu</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Réhabilitation de l'Hôpital Général de Référence de Makala: salle moderne de réanimation, Urgence Médecine interne, pédiatrieque, Churirgie, Gyneco et Réhabilitation du pavillon</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction d'une nouvelle maternité de Monaco à l'Hôpital Général de Référence de Maluku 1</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
        
        <div class="col-md-12 mb-3">
            <h2 class="ubuntu-font" style="color: #febc11;"><b>Construction d'un funérarium moderne à l'Hôpital
Général de Référence de Kinshasa, ex-Mama Yemo</b></h2>
                <div class="row">
                    <div class="col-md-6"></div>
                    <div class="col-md-6"></div>
                </div>
        </div>
        
    </div>
  
</div>


	<?php include 'includes/footer.php'; ?>
</main>