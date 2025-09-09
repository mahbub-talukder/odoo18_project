<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set headers to handle AJAX requests
header('Content-Type: application/json');

$response = ['success' => false, 'errors' => []];

// Check if form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $_POST["name"] ?? '';
    $email = $_POST["email"] ?? '';
    $phone = $_POST["phone"] ?? '';
    $message = $_POST["message"] ?? '';
    
    // Validate form data
    $valid = true;
    $errors = [];
    
    if (empty($name)) {
        $valid = false;
        $errors['name'] = "Le nom est requis";
    }
    
    if (empty($email)) {
        $valid = false;
        $errors['email'] = "L'email est requis";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $valid = false;
        $errors['email'] = "Format d'email invalide";
    }
    
    if (empty($phone)) {
        $valid = false;
        $errors['phone'] = "Le téléphone est requis";
    }
    
    if (empty($message)) {
        $valid = false;
        $errors['message'] = "Le message est requis";
    }
    
    if ($valid) {
        // Email settings
        $to = "thobilesema@gmail.com"; // Your Gmail address
        $from_email = "arogyahealingcentre01@gmail.com"; // Your Gmail address
        $from_name = "ACP Website Contact";
        $subject = "Nouveau message de contact - ACP Website";

        try {
            // Include PHPMailer
            require 'PHPMailer/src/PHPMailer.php';
            require 'PHPMailer/src/SMTP.php';
            require 'PHPMailer/src/Exception.php';

            $mail = new PHPMailer\PHPMailer\PHPMailer(true);

            // Server settings
            $mail->isSMTP();
            $mail->Host = 'smtp.gmail.com';
            $mail->SMTPAuth = true;
            $mail->Username = 'arogyahealingcentre01@gmail.com'; // Your Gmail
            $mail->Password = 'ajew gbyh incq bqnj'; // Your Gmail App Password
            $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port = 587;

            // Recipients
            $mail->setFrom($from_email, $from_name);
            $mail->addAddress($to);
            $mail->addReplyTo($email, $name);

            $email_text2 = '
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Nouveau message de contact</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px;">
    <div style="max-width: 600px; margin: auto; background: #ffffff; border: 1px solid #ddd; border-radius: 8px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <h2 style="color: #0805b1; text-align: center; margin-top: 0;">
            <svg style="width: 24px; height: 24px; vertical-align: middle; margin-right: 8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            Nouveau message de contact
        </h2>
        <div style="margin-top: 20px;">
            <p style="margin: 10px 0;">
                <strong style="color: #ac0a06; display: flex; align-items: center;">
                    <svg style="width: 20px; height: 20px; margin-right: 8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                    Nom:
                </strong><br>
                <span style="color: #333;">' . htmlspecialchars($name) . '</span>
            </p>
            <p style="margin: 10px 0;">
                <strong style="color: #ac0a06; display: flex; align-items: center;">
                    <svg style="width: 20px; height: 20px; margin-right: 8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
                    Email:
                </strong><br>
                <span style="color: #333;">' . htmlspecialchars($email) . '</span>
            </p>
            <p style="margin: 10px 0;">
                <strong style="color: #ac0a06; display: flex; align-items: center;">
                    <svg style="width: 20px; height: 20px; margin-right: 8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
                    Téléphone:
                </strong><br>
                <span style="color: #333;">' . htmlspecialchars($phone) . '</span>
            </p>
            <p style="margin: 10px 0;">
                <strong style="color: #ac0a06; display: flex; align-items: center;">
                    <svg style="width: 20px; height: 20px; margin-right: 8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    Message:
                </strong><br>
                <div style="background: #f9f9f9; border-left: 4px solid #f5d804; padding: 10px 15px; color: #0805b1; border-radius: 4px; margin-top: 5px;">
                    ' . nl2br(htmlspecialchars($message)) . '
                </div>
            </p>
        </div>
        <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;">
        <p style="font-size: 12px; text-align: center; color: #999;">
            ⛔ Ceci est un message automatique. Veuillez ne pas y répondre directement.
        </p>
    </div>
</body>
</html>';

            // Content
            $mail->isHTML(true);
            $mail->Subject = $subject;
            $mail->Body = $email_text2;  // Use the better formatted template
            $mail->AltBody = strip_tags($message);  // Plain text version

            $mail->send();
            $response['success'] = true;
            $response['message'] = 'Message envoyé avec succès!';

        } catch (Exception $e) {
            $response['success'] = false;
            $response['message'] = "Erreur d'envoi: " . $mail->ErrorInfo;
        }
    } else {
        $response['success'] = false;
        $response['message'] = 'Veuillez corriger les erreurs:';
        $response['errors'] = $errors;
    }
}

echo json_encode($response);
?>