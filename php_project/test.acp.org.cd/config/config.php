<?php
// Automatically detect base URL
$protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') ? "https" : "http";
$host = $_SERVER['HTTP_HOST'];
$folder = trim(dirname($_SERVER['SCRIPT_NAME']), '/\\');

define('BASE_URL', $protocol . '://' . $host . '/' . $folder);