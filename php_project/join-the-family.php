<?php
$page = 'join-the-family';          // used to load home.css
$title = 'Rejoingez-nous';
include 'includes/header.php';
?>

<main>
  <div style="height: 160px;"></div>

  <div>
    <div class="image-crop-container">
      <img src="<?= BASE_URL ?>/assets/img/woman-holding-card.png" class="focus-right-image" alt="">
    </div>

    <div class="container card-box" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
      <div class="cards-parent">
        <img src="<?= BASE_URL ?>/assets/img/front-card.png" class="card-back" alt="" data-aos="zoom-in" data-aos-delay="500" data-aos-duration="1000">
        <img src="<?= BASE_URL ?>/assets/img/back-card.png" class="card-back" alt="" data-aos="zoom-in" data-aos-delay="1000" data-aos-duration="1000">

      </div>
    </div>

    <div class="container bottom-blue" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">

      <div class="bottom-blue-content">
        <p class="bottom-blue-paragraph"><b>Adhérez à l'ACP et découvrez les nombreux avantages de notre programme de membres.</b></p>
        <img src="<?= BASE_URL ?>/assets/img/right-arrow-icon-picture.png" class="icon" alt="">
      </div>

    </div>

  </div>

  <div class="form-big-parent">

    <div class="container">

      <div class="row">
        <div class="col-12 col-md-6 pe-0 pe-md-5" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
          <div class="genity">Une carte, mille opportunités</div>
          <div class="topicstyle-1">Rejoignez la famille</div>
          <div class="d-flex align-items-center gap-3">
            <img src="<?= BASE_URL ?>/assets/img/logo/acp-logo-refined.png" alt="Logo" class="small-logo-logo" style="height: 60px;" />

            <div>
              <div class="acp-contain" data-aos="fade-down" data-aos-delay="500" data-aos-duration="1000">
                <div class="letter letter-a">A</div>
                <div class="letter letter-c">C</div>
                <div class="letter letter-p">P</div>
              </div>
            </div>
          </div>
          <div class="paragraph-to-form" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">Adhérez à l'ACP et découvrez les nombreux avantages de notre programme de membres. Votre carte personnelle vous ouvrira les portes à des services de valeur, des réductions chez nos partenaires et la possibilité de participer activement à la croissance de la RDC. Saisissez cette chance de faire partie du changement positif !</div>
        </div>

        <div class="col-12 col-md-6" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000">

          <form id="joinFamilyForm">
            <div class="row">
              <div class="col-12 mb-3">
                <label for="full_name" class="form-label-custom">Nom complet</label>
                <input type="text" id="full_name" name="full_name" class="form-input-custom" placeholder="" required>
              </div>
            </div>

            <div class="row">
              <div class="col-12 col-md-6 mb-3">
                <label for="email" class="form-label-custom">Email</label>
                <input type="email" id="email" name="email" class="form-input-custom" placeholder="" required>
              </div>

              <div class="col-12 col-md-6 mb-3">
                <label for="phone" class="form-label-custom">Téléphone</label>
                <input type="tel" id="phone" name="phone" class="form-input-custom" placeholder="" required>
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label class="form-label-custom">Sexe</label>
                <div class="d-flex gap-3 mt-2">
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="x_studio_gender" id="genderMale" value="male" required>
                    <label class="form-check-label" for="genderMale">
                      Male
                    </label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="x_studio_gender" id="genderFemale" value="female" required>
                    <label class="form-check-label" for="genderFemale">
                      Female
                    </label>
                  </div>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label for="profession" class="form-label-custom">Profession</label>
                <input type="text" id="profession" name="profession" class="form-input-custom" placeholder="" required>
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label for="place_of_birth" class="form-label-custom">Lieu de naissance</label>
                <input type="text" id="place_of_birth" name="place_of_birth" class="form-input-custom" placeholder="" required>
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label for="nationality_id" class="form-label-custom">Pays</label>
                <select id="nationality_id" name="nationality_id" class="form-select-custom" required>
                  <option value="">Select Country</option>
                </select>
              </div>
            </div>

            <div class="row">
              <div class="col-12 mb-3">
                <label for="date_of_birth" class="form-label-custom">Date de naissance</label>
                <input type="date" id="date_of_birth" name="date_of_birth" class="form-input-custom" required>
              </div>
            </div>

            <div class="row">
              <div id="formMessage" class="mt-3">
              </div>
            </div>

            <div class="row">
              <div class="col-12 col-md-6 mb-3">
                <button type="submit" class="submit-button">Soumettre</button>
              </div>

              <div class="col-12 col-md-6 mb-3" data-aos="fade-top" data-aos-delay="1500" data-aos-duration="1000">
                <img src="<?= BASE_URL ?>/assets/img/new-hand-card-hold.png" class="hand-card" alt="decoration" />
              </div>
            </div>
           
          </form>
        </div>

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

    document.addEventListener('DOMContentLoaded', function() {
        const nationalitySelect = document.getElementById('nationality_id');
        const formMessage = document.getElementById('formMessage');
        const joinFamilyForm = document.getElementById('joinFamilyForm');

        // Function to fetch countries from Odoo API
        async function fetchCountries() {
            try {
                const response = await fetch('http://localhost:8071/api/get_countries', {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }); // Adjust Odoo URL if necessary
                const countries = await response.json();
                countries.forEach(country => {
                    const option = document.createElement('option');
                    option.value = country.id;
                    option.textContent = country.name;
                    nationalitySelect.appendChild(option);
                });
            } catch (error) {
                console.error('Error fetching countries:', error);
                formMessage.className = 'alert alert-danger';
                formMessage.textContent = 'Error loading countries. Please try again later.';
            }
        }

        // Fetch countries on page load
        fetchCountries();

        // Handle form submission
        joinFamilyForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            formMessage.textContent = ''; // Clear previous messages
            formMessage.className = '';

            const formData = new FormData(joinFamilyForm);
            const data = {};
            for (let [key, value] of formData.entries()) {
                data[key] = value;
            }

            // Convert date to Odoo's expected format (YYYY-MM-DD)
            if (data.date_of_birth) {
                data.date_of_birth = new Date(data.date_of_birth).toISOString().split('T')[0];
            }
            console.log(data);

            try {
                const response = await fetch('http://localhost:8071/api/submit_form', { // Adjust Odoo URL if necessary
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                console.log('result',result);

                if (result.success) {
                    formMessage.className = 'alert alert-success';
                    formMessage.textContent = result.message;
                    joinFamilyForm.reset(); // Clear the form on success
                    // Re-fetch countries if needed, or ensure the dropdown is correctly reset
                    nationalitySelect.innerHTML = '<option value="">Select Country</option>';
                    fetchCountries();
                } else {
                    formMessage.className = 'alert alert-danger';
                    formMessage.textContent = result.error;
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                formMessage.className = 'alert alert-danger';
                formMessage.textContent = 'An unexpected error occurred. Please try again.';
            }
        });
    });
  </script>
</main>