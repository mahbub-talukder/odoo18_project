<?php
$page = 'deputies';          // used to load home.css
$title = 'Qui Sommes -Nous';
include 'includes/header.php';


$executive_team = [
    /**['name' => 'Charles', 'surname' => 'MBUTAMUNTU', 'position' => 'secrétaire général', 'picture' => null] */
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    ['name' => 'Jean', 'surname' => 'KABILA', 'position' => 'Deputy Minister', 'picture' => null],
    
];
?>

<main>

    <div style="height: 160px;"></div>


    <div class="container text-center py-5">
  
  <!-- Image -->
  <div class="mb-4 logo-paren">
    <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-new.png" alt="Logo" class="" style="width:100px;" />
  </div>

  <!-- Content Div -->
  <div class="mb-3 p-3 d-inline-block">
    <h1 class="d-inline-block topic">Nos Députés </h1>
    <div class="line-something my-3">
                        <div class="line-blue"></div>
                        <div class="line-brown"></div>
                        <div class="line-yellow"></div>
                    </div>
  </div>

  <!-- Paragraph -->
  <p class="mt-3 mx-auto paragraph-text-1">
  Bienvenue sur la page officielle des Députés de l’Action Commune pour le Progrès (ACP).
  Nos représentants à l’Assemblée nationale œuvrent chaque jour pour défendre les intérêts de notre peuple et bâtir un avenir meilleur pour la République Démocratique du Congo
</p>

</div>


<div class="container executive-team-list py-4">
  <hr>
  <div class="row">
    <?php foreach ($executive_team as $member): ?>
      <div class="col-6 col-md-3 mb-4">
        <a href="<?= BASE_URL ?>deputies-individual.php" style="text-decoration: none; color: inherit; display: block;">
          <div class="team-card">
            <div class="team-img-wrapper">
              <?php if ($member['picture']): ?>
                <img src="<?= htmlspecialchars($member['picture']) ?>" alt="Profile of <?= htmlspecialchars($member['name']) ?>">
              <?php else: ?>
                <img src="<?= BASE_URL ?>/assets/img/deputy-profile-icon.png" class="" alt="">
              <?php endif; ?>
            </div>
            <div class="team-title">Hon.</div>
            <div class="team-name">
              <?= htmlspecialchars($member['name']) . ' ' . strtoupper(htmlspecialchars($member['surname'])) ?>
            </div>
            <div class="team-position"><?= htmlspecialchars($member['position']) ?></div>
          </div>
        </a>
      </div>
    <?php endforeach; ?>
  </div>
</div>


    <div class="container d-flex justify-content-center">
  <div class="p-3 text-center" style="width: 300px;">
    <!-- Image on top -->
    <img src="<?= BASE_URL ?>/assets/img/see-more-icon.png" class="img-fluid mb-1" alt="" width="50">
    
    <!-- Text below -->
    <div>
      <p class="team-title">VOIR PLUS</p>
    </div>
  </div>
</div>


    <?php include 'includes/footer.php'; ?>
</main>