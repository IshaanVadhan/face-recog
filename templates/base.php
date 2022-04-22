<?php
echo "
<!DOCTYPE html>
<html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Face Recognition - Attendance</title>
        <link rel=\"stylesheet\" href=\"{{ url_for('static',filename='css/style.css') }}\">
        <script src=\"https://kit.fontawesome.com/a076d05399.js\"></script>
        <script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>
    </head>
    <body>
        <nav class=\"navbar\">
            <div class=\"max-width\">
                <div class=\"logo\"><a href=\"#\">Face<span>Recog</span></a></div>
                <ul class=\"menu\">
                    <li><a href=\"{{ url_for('index') }}\" class=\"menu-btn\">Home</a></li>
                    <li><a href=\"#about\" class=\"menu-btn\">About</a></li>
                    <li><a href=\"{{ url_for('teams') }}\" class=\"menu-btn\">Teams</a></li>
                    <li><a href=\"#contact\" class=\"menu-btn\">Contact</a></li>
                </ul>
                <div class=\"buttons\">
                    <div class=\"dark-mode-btn\">
                        <i class=\"fas fa-sun\" id=\"theme-button\"></i>
                    </div>
                    <div class=\"menu-btn\">
                        <i class=\"fas fa-bars\"></i>
                    </div>
                </div>
            </div>
        </nav>";
?>