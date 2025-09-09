<?php
$page = 'home';          // used to load home.css
$title = 'Welcome Home';
include 'includes/header.php';
?>

<!-- Floating Logo -->
 <div >
<main class="position-relative">

    <div style="height: 160px;"></div>
    <img src="<?= BASE_URL ?>/assets/img/background-person.png" class="decorative-img1" alt="decoration" />

    <div class="container position-relative first-parent">

        <img src="<?= BASE_URL ?>/assets/img/building-decorative.png" class="decorative-img2" alt="decoration" />

        <div class="row">
            <div class="col-12 col-md-6">
                <div style="margin-bottom: 100px;">
                  <h1 class="topic"><span style="color: blue;">A</span>lliance des <span style="color: brown;">C</span>ongolais <span style="color: yellow;">P</span>rogressistes</h1>

                <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
                </div>
                <div class="button-wrapper">
                    <a href="#" class="btn-button">rejoindre l'acp</a>
                </div>
            </div>
            <div class="col-12 col-md-6 position-relative mb-5">
                <video class="looping-video" autoplay muted loop playsinline>
                    <source src="<?= BASE_URL ?>/assets/video/video-loop-3.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>

        

    </div>

    <div class="container second-parent">
            <div class="container blended-wrapper position-relative">
  <img src="<?= BASE_URL ?>/assets/img/listening-song.png" alt="Left Image" class="background-image">

  <div class="blue-gradient-overlay">
    <div class="content-on-blue">
      <h2>HYMNE DE L' ALLIANCE DES CONGOLAIS PROGRESSISTES</h2>
      <div class="music-player">
  <audio id="music-audio" src="your-audio-file.mp3"></audio>

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
      <div></div>
    </div>
  </div>
</div>
                
            <div class="container mt-5">
  <div class="row g-2">
    <div class="col-12 col-md-4">
      <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/justice-part.png');">
      </div>
    </div>
    
    <div class="col-12 col-md-4">
      <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/travail.png');">
      </div>
    </div>
    
    <div class="col-12 col-md-4">
      <div class="justice-card" style="background-image: url('<?= BASE_URL ?>/assets/img/progres.png');">
      </div>
    </div>
  </div>
</div>

  <div class="row">

  </div>

            

    </div>

    <div class="third-parent position-relative">
        <img src="<?= BASE_URL ?>/assets/img/background-person.png" class="decorative-img1" alt="decoration" />
        <img src="<?= BASE_URL ?>/assets/img/flag.png" class="decorative-third-img1" alt="decoration" />
        <div class="container">
            <div class="row">
                <div class="col-12 col-md-6"> 
                    <p class="genity">
                        Gentiny
                    </p>
                    
                    <div>
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

                    <p class="mini-size-paragraph">Homme d'action, le Camarade Gentiny NGOBILA MBAKA a fondé <b>l'Alliance des Congolais Progressistes (ACP)</b> avec une vision claire : </p>

                    <p class="mini-size-paragraph">libérer le peuple congolais de la pauvreté et combattre la corruption qui freine notre développement.</p>
                    <p class="mini-size-paragraph">Ce mouvement national, ouvert à la diaspora internationale, invite chaque Congolais à s'approprier ce combat essentiel pour notre avenir.</p>
                    <a href="#" class="profile-button">PROFILE</a>
            </div>


                <div class="col-12 col-md-6">
            <img src="<?= BASE_URL ?>/assets/img/human-third.png" class="human-in-blue" alt="decoration" />        
            </div>  

            </div>
        </div>
    </div>

    <div class="form-big-parent">

    <div class="container">

        <div class="row">
            <div class="col-12 col-md-6 pe-0 pe-md-5">
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
               <div class="paragraph-to-form">Adhérez à l'ACP et découvrez les nombreux avantages de notre programme de membres. Votre carte personnelle vous ouvrira les portes à des services de valeur, des réductions chez nos partenaires et la possibilité de participer activement à la croissance de la RDC. Saisissez cette chance de faire partie du changement positif !</div>
            </div>

            <div class="col-12 col-md-6">

                <div>
                    <div class="row">
  <div class="col-12 col-md-6 mb-3">
    <label for="input1" class="form-label-custom">Name</label>
    <input type="text" id="input1" class="form-input-custom" placeholder="">
  </div>

  <div class="col-12 col-md-6 mb-3">
    <label for="input2" class="form-label-custom">Votre Post Nom</label>
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
    <label for="input1" class="form-label-custom">Votre sexe</label>
    <input type="text" id="input1" class="form-input-custom" placeholder="">

    <button class="submit-button">Soumettre</button>

  </div>

    <div class="col-12 col-md-6 mb-3">
        <img src="<?= BASE_URL ?>/assets/img/hand-card.png" class="human-in-blue" alt="decoration" />
    </div>

</div>

                </div>

            </div>

    </div>
</div>
</div>

<div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
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

</main>

</div>

