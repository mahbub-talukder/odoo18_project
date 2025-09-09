<?php
$page = 'news';          // used to load home.css
$title = 'News';
include 'includes/header.php';
?>

<main>

    <div style="height: 160px;"></div>
	
<div class="container my-4">
  <div class="row">
    <div class="col-md-6 mb-3">
      <div class="p-3">
	  
		<div>
			<div class="d-inline-block">
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
    </div>
    <div class="col-md-6 mb-3">
      <div class="search-container d-flex justify-content-center justify-content-md-end">
    <div class="input-group w-100 w-md-auto" style="max-width: 400px;">
      <span class="input-group-text bg-white">
        <!-- Search SVG Icon -->
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 21l-4.35-4.35m1.85-5.15a7 7 0 11-14 0 7 7 0 0114 0z"/>
        </svg>
      </span>
      <input type="text" class="form-control" placeholder="Search...">
    </div>
  </div>
    </div>
  </div>
</div>

<div class="container my-4">
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
      ],
      [
        'title' => 'Article 4',
        'description' => 'La description de larticle sera collée ici. Ceci est juste un espace réservé une fois terminé.',
        'image' => BASE_URL . '/assets/img/news-1.png'
      ]
    ];

    foreach ($newsList as $news) {
      echo '
        <div class="col-12 col-md-6 col-lg-3">
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
	
	<?php include 'includes/footer.php'; ?>
	
	
	
</main>