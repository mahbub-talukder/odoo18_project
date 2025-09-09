<?php
$page = 'home';          // used to load home.css
$title = 'Alliance des Congolais Progressistes';
include 'includes/header.php';
?>

<!-- Floating Logo -->
 <div >
<main class="position-relative overflow-hidden">

  <div id="video-overlay" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: black; z-index: 9999;">
  <video id="intro-video" autoplay muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
    <source src="<?= BASE_URL ?>/assets/video/intro-video.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>



  <div id="lyrics-popup" class="lyrics-pop-overlay">
  <div class="lyrics-pop-content">
    <span class="lyrics-pop-close" onclick="closeLyricsPopup()">✖</span>
    <div class="lyrics-pop-inner">
      <h2>HYMNE DE L' ALLIANCE DES CONGOLAIS PROGRESSISTES</h2>
      
      <!-- Add more content to test scrolling -->
      <p>ACP parti des vaillants</p>
<p>ACP parti des battants</p>
<p>Alliance des congolais progressistes</p>
<p>Nous jurons avec loyauté</p>
<p>Nous jurons, nous te promettons</p>
<p>De toujours bien protéger ta renommée</p>
<p>Gagner le grand pari de l'émergence</p>
<p>C'est ça notre défi en permanence</p>
<p>Liberté, égalité, démocratie, développement</p>
<p>Nous sommes fiers d'être Acp</p>
<p>Liberté, égalité, démocratie, développement</p>
<p>ACP allons de l'avant</p>
<p>A nos vaillants soldats partis en guerre</p>
<p>Que l'amour sacré de la patrie vous accompagne.</p>
<p>FARDC tenez bon, ne jamais baisser les bras</p>
<p>Hourra ! Résistez à l'ennemi</p>
<p>Congolais bravons la peur, nous devons affûter nos armes</p>
<p>Hourra ! Protégeons la patrie.</p>
<p>Comme on enfouit une épée dans un fourreau,</p>
<p>Gardons le Congo notre grand trésor.</p>
<p>Le bien-être du Congolais est le socle de notre lutte.</p>
<p>Viva ! Notre belle ACP.</p>
<p>La la la la la la la</p>
<p>La la la la la la la</p>
<p>La la la la la la la</p>
<p>La la la la la la la</p>
    </div>
  </div>
</div>



    <div style="height: 160px;"></div>
    <img src="<?= BASE_URL ?>/assets/img/deco-back-man.png" class="decorative-img1" alt="decoration" />

    <div class="container position-relative first-parent">

        <!-- <img src="<?= BASE_URL ?>/assets/img/building-decorative.png" class="decorative-img2" alt="decoration" /> -->

        <div class="row">
            <div class="col-12 col-md-6" data-aos="fade-down" data-aos-delay="500">
                <div style="margin-bottom: 30px;" class="d-inline-block">
                  <div class="topic d-inline-block" style="display: inline;"><span style="color: blue;">A</span>lliance des <span style="color: brown;">C</span>ongolais <span style="color: yellow;">P</span>rogressistes</div>

                <div style="width:70%;">
                  <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
                </div>
                </div>
                <div class="button-wrapper">
                    <a href="<?= BASE_URL ?>join-the-family.php" class="btn-button" data-aos="zoom-in" data-aos-delay="2500">Rejoignez-nous!</a>
                </div>
            </div>
            <div class="col-12 col-md-6 position-relative mb-5" data-aos="fade-up" data-aos-delay="1500">
                <video class="looping-video" autoplay muted loop playsinline>
                    <source src="<?= BASE_URL ?>/assets/video/3ans-vid.mp4" type="video/mp4">
                    Votre navigateur ne prend pas en charge la balise vidéo.
                </video>
            </div>
        </div>

        

    </div>

    <div class="container second-parent">
            <div class="container blended-wrapper position-relative" data-aos="zoom-in" data-aos-delay="1000">
  <img src="<?= BASE_URL ?>/assets/img/next-to-hym-back-2.png" alt="Left Image" class="background-image">

  <div class="blue-gradient-overlay">
    <div class="content-on-blue">
      <h2 class="blue-back-heading"><b>HYMNE DE <br> L'ALLIANCE DES CONGOLAIS PROGRESSISTES</b></h2>
      <div class="music-player">
  <audio id="music-audio" src="<?= BASE_URL ?>/assets/music/hymneacp.mp3"></audio>

  <button class="music-play-btn" id="play-btn" aria-label="Play">
    <svg id="play-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" viewBox="0 0 16 16">
      <path d="M6 4.5v7l6-3.5-6-3.5z"/>
    </svg>
    <svg id="pause-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" viewBox="0 0 16 16" style="display: none;">
      <path d="M5 3.5A.5.5 0 0 1 5.5 3h1a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-9zm4 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-9z"/>
    </svg>
  </button>

  <span class="music-time" id="time-display">0:00 / 0:00</span>

  <input type="range" class="music-progress" id="progress-bar" min="0" max="100" value="0">

  <button class="music-volume-btn" id="mute-btn" aria-label="Mute">
    <svg id="volume-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" viewBox="0 0 16 16">
      <path d="M11.536 14.01A8 8 0 0 0 13 8a8 8 0 0 0-1.464-4.01l-.867.5A7 7 0 0 1 12 8a7 7 0 0 1-1.331 4.01l.867.5z"/>
      <path d="M8.707 11.293a1 1 0 0 1 0 1.414l-.707.707A1 1 0 0 1 7 13.414V2.586a1 1 0 0 1 1.707-.707l.707.707a1 1 0 0 1 0 1.414l-.707.707V10.586l.707.707zM6 4H4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h2V4z"/>
    </svg>
    <svg id="muted-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" viewBox="0 0 16 16" style="display: none;">
      <path d="M9.646 4.354a.5.5 0 0 0-.708-.708L6.5 6.293 3.854 3.646a.5.5 0 1 0-.708.708L5.793 7 3.146 9.646a.5.5 0 0 0 .708.708L6.5 7.707l2.646 2.647a.5.5 0 0 0 .708-.708L7.207 7l2.439-2.646z"/>
    </svg>
  </button>
</div>
      <div class="lyrics-button-parent"> <button class="lyrics-button" onclick="showLyricsPopup()">voir les paroles ></button></div>
    </div>
  </div>
</div>
                
            <div class="container justice-container">
                <div class="row g-1">
                    <div class="col-12 col-md-4 mb-1 mb-md-0" data-aos="fade-down" data-aos-delay="500">
                        <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/justice-2.png');">
                        </div>
                    </div>
                    
                    <div class="col-12 col-md-4 mb-1 mb-md-0" data-aos="fade-up" data-aos-delay="1000">
                        <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/travail-2.png');">
                        </div>
                    </div>
                    
                    <div class="col-12 col-md-4" data-aos="fade-down" data-aos-delay="1500">
                        <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/progres-2.png');">
                        </div>
                    </div>
                </div>
            </div>

  <div class="row">

  </div>

            

    </div>

    <div class="third-parent position-relative overflow-hidden">
        <img src="<?= BASE_URL ?>/assets/img/deco-back-man.png" class="decorative-img1-2" alt="decoration" />
        <img src="<?= BASE_URL ?>/assets/img/flag.png" class="decorative-third-img1" alt="decoration" />
        <div class="container">
            <div class="row">
                <div class="col-12 col-md-6" data-aos="fade-up" data-aos-delay="1500"> 
                    <p class="genity">
                        Gentiny
                    </p>
                    
                    <div class="d-inline-block">
                    <h2 class="topicstyle-1">
                        NGOBILA MBAKA
                    </h2>

                    <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
                    </div>

                    <div style="height: 20px;">

                    </div>

                    <!--<p class="mini-size-paragraph">Homme d'action, le camarade Gentiny NGOBILA MBAKA a fondé <b>l'Alliance des Congolais Progressistes (ACP)</b> avec une vision claire : </p>

                    <p class="mini-size-paragraph">libérer le peuple congolais de la pauvreté et combattre la corruption qui freine notre développement.</p>
                    <p class="mini-size-paragraph">Ce mouvement national, ouvert à la diaspora internationale, invite chaque Congolais à s'approprier ce combat essentiel pour notre avenir.</p>-->
                    <p class="mini-size-paragraph" align="justify">C’est dans le vaste tableau politique de la République Démocratique du Congo, qu’une figure émerge avec une détermination inébranlable : <b>Gentiny Ngobila Mbaka.</b><br>
                        Acteur politique de gauche,<< il incarne l'espoir d'un peuple en quête de renouveau >>.  Il voit le jour le 20 septembre 1963 en RDC.
                        Après avoir obtenu une licence en administration et gestion du personnel au <b>C</b>onservatoire <b>N</b>ational des <b>A</b>rts et <b>M</b>étiers (CNAM) de Paris, <b>GENTINY NGOBILA</b> se lance dans le monde des affaires créant plusieurs entreprises, démontrant ainsi son esprit entrepreneurial et sa capacité à innover. <br>
                        Dans les années 1990, il fait le saut vers la politique, où il occupe divers postes successivement, notamment celui de député en 2011, vice-ministre de l’agriculture, PCA à l’Office des routes, Député National en 2019, Commissaire spécial au Maï Ndombe.</br>
                        En avril 2019, il est élu gouverneur de la ville-province de Kinshasa, un rôle une fonction qu'il embrasse avec détermination et passion. Sous sa direction, la capitale congolaise connaît des transformations notables, témoignant de son engagement envers le bien-être de ses concitoyens.
                        En 2022, il fonde l'Alliance des Congolais Progressistes, un mouvement politique qui rassemble plus de 100 000 membres au stade de Martyre lors de sa sortie officiel, reconnu comme un véritable parti de masse.</br> 
                        Cet engouement populaire découle de la générosité et de la loyauté organique envers son prochain, des valeurs que Gentiny Ngobila incarne avec brio. Ces valeurs, qui nous unissent, sont le socle sur lequel repose son action politique. Elles sont le fil conducteur de son engagement à raviver l'espoir et à bâtir un avenir meilleur pour notre mère patrie. 
                        Gentiny Ngobila Mbaka n'est pas seulement un homme d'État ; il est un bâtisseur de ponts entre les générations et un fervent défenseur d'un Congo prospère et solidaire. Dans un monde en constante évolution, sa vision et son dévouement sont des phares qui éclairent le chemin vers un avenir prometteur pour tous les Congolais.


                    </p>
                    <a href="<?= BASE_URL ?>authors.php" class="profile-button" data-aos="fade-right" data-aos-delay="2500">Profil du Président</a>
            </div>


                <div class="col-12 col-md-6"data-aos="fade-down" data-aos-delay="1500">
            <img src="<?= BASE_URL ?>/assets/img/human-third.png" class="human-in-blue" alt="decoration" />        
            </div>  

            </div>
        </div>
    </div>
    
    <div class="container my-4">
        <div class="row">
            <div class="col-md-6">
          <div class="d-inline-block mb-3">
                    <h2 class="topicstyle-1 blue-text">
                        Dernières nouvelles
                    </h2>

                    <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
                    </div>
      </div>
        </div>
  <div class="row">
      
      
    <?php
    // Example list of news
    $newsList = [
      [
        'title' => 'Article 1',
        'description' => 'La description de larticle sera collée ici. Ceci est juste un espace réservé une fois terminé.',
        'image' => BASE_URL . '/assets/img/news-1.png'
      ],
      [
        'title' => 'Article 2',
        'description' => 'La description de larticle sera collée ici. Ceci est juste un espace réservé une fois terminé.',
        'image' => BASE_URL . '/assets/img/news-1.png'
      ],
      [
        'title' => 'Article 3',
        'description' => 'La description de larticle sera collée ici. Ceci est juste un espace réservé une fois terminé.',
        'image' => BASE_URL . '/assets/img/news-1.png'
      ]
    ];

    foreach ($newsList as $news) {
      echo '
        <div class="col-12 col-md-6 col-lg-4">
          <div class="news-item">
            <div class="news-top">
              <h5 class="blue-text news-title-one poppins-font">' . htmlspecialchars($news['title']) . '</h5>
              <p class="news-description-one ubuntu-font">' . htmlspecialchars($news['description']) . '</p>
            </div>
            <div class="news-image">
              <img src="' . $news['image'] . '" alt="News Image">
            </div>
          </div>
        </div>
      ';
    }
    ?>
  </div>
</div>

    <div class="form-big-parent">

    <div class="container">

        <div class="row">
            <div class="col-12 col-md-6 pe-0 pe-md-5 " >
               <div class="genity">Une carte, mille opportunités</div>
               <div class="topicstyle-1">Rejoignez la famille</div>
               <div class="d-flex align-items-center gap-3">
  <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-refined.png" alt="Logo" class="small-logo-logo" style="height: 60px;" />

  <div>
    <div class="acp-contain">
  <div class="letter letter-a">A</div>
  <div class="letter letter-c">C</div>
  <div class="letter letter-p">P</div>
</div>
  </div>
</div>
               <div class="paragraph-to-form">Adhérez à ACP et découvrez les nombreux avantages de notre programme de membres. Votre carte personnelle vous ouvrira les portes à des services de valeur, des réductions chez nos partenaires et la possibilité de participer activement à la croissance de la RDC. Saisissez cette chance de faire partie du changement positif !</div>
            </div>

            <div class="col-12 col-md-6" data-aos="fade-down" data-aos-delay="500">

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
    <label for="input1" class="form-label-custom">Adresse Email</label>
    <input type="text" id="input1" class="form-input-custom" placeholder="">
  </div>

  <div class="col-12 col-md-6 mb-3">
    <label for="input2" class="form-label-custom">Téléphone</label>
    <input type="tel" id="input2" class="form-input-custom" placeholder="">
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

    <div class="col-12 col-md-6 mb-3">
        <img src="<?= BASE_URL ?>/assets/img/new-hand-card-hold.png" class="hand-card" alt="decoration"  />
    </div>

</div>

                </div>

            </div>

    </div>
</div>
</div>



 <?php include 'includes/footer.php'; ?>      


  <script>
  const audio = document.getElementById("music-audio");
  const playBtn = document.getElementById("play-btn");
  const playIcon = document.getElementById("play-icon");
  const pauseIcon = document.getElementById("pause-icon");
  const muteBtn = document.getElementById("mute-btn");
  const volumeIcon = document.getElementById("volume-icon");
  const mutedIcon = document.getElementById("muted-icon");
  const timeDisplay = document.getElementById("time-display");
  const progressBar = document.getElementById("progress-bar");

  function formatTime(seconds) {
    const min = Math.floor(seconds / 60);
    const sec = Math.floor(seconds % 60).toString().padStart(2, "0");
    return `${min}:${sec}`;
  }

  audio.addEventListener("loadedmetadata", () => {
    timeDisplay.textContent = `0:00 / ${formatTime(audio.duration)}`;
  });

  playBtn.addEventListener("click", () => {
    if (audio.paused) {
      audio.play();
      playIcon.style.display = "none";
      pauseIcon.style.display = "inline";
    } else {
      audio.pause();
      playIcon.style.display = "inline";
      pauseIcon.style.display = "none";
    }
  });

  muteBtn.addEventListener("click", () => {
    audio.muted = !audio.muted;
    volumeIcon.style.display = audio.muted ? "none" : "inline";
    mutedIcon.style.display = audio.muted ? "inline" : "none";
  });

  audio.addEventListener("timeupdate", () => {
    progressBar.value = (audio.currentTime / audio.duration) * 100;
    timeDisplay.textContent = `${formatTime(audio.currentTime)} / ${formatTime(audio.duration)}`;
  });

  progressBar.addEventListener("input", () => {
    audio.currentTime = (progressBar.value / 100) * audio.duration;
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

  <script>
    function showLyricsPopup() {
  document.getElementById('lyrics-popup').style.display = 'flex';
}

function closeLyricsPopup() {
  document.getElementById('lyrics-popup').style.display = 'none';
}
  </script>

  <script>
  const overlay = document.getElementById('video-overlay');
  const video = document.getElementById('intro-video');

  // Hide overlay after video ends
  video.addEventListener('ended', () => {
    overlay.style.display = 'none';
  });

  // Optional: Hide after a few seconds if needed
  setTimeout(() => {
    overlay.style.display = 'none';
  }, 11000); // 6 seconds fallback
</script>

</main>

</div>

