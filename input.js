<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AI Phishing Email Detector Pro</title>

<link rel="stylesheet"
href="{{ url_for('static', filename='css/style.css') }}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

</head>

<body>

<nav>

<div class="logo">

🛡 AI Phishing Detector Pro

</div>

<ul>

<li>Dashboard</li>
<li>Features</li>
<li>Documentation</li>

</ul>

</nav>

<section class="hero">

<h1>

Detect Phishing Emails with
<span>Gemini AI</span>

</h1>

<p>

Upload an Email • Analyze URLs • AI Threat Detection • Generate Security Report

</p>

<div class="badges">

<span>🤖 Gemini AI</span>

<span>📧 .eml Upload</span>

<span>📊 Analytics</span>

<span>📄 PDF Report</span>

</div>

</section>

<div class="main-card">

<form action="/analyze"

method="POST"

enctype="multipart/form-data">

<div class="upload-box">

<h2>

📧 Upload Email File

</h2>

<input

type="file"

name="emailfile"

accept=".eml"

required>

<p>

Drag & Drop Supported

</p>

</div>

<div class="divider">

OR

</div>

<div>

<h2>

✍ Paste Email Content

</h2>

<textarea

name="emailtext"

placeholder="Paste Email Here..."></textarea>

</div>

<button>

🚀 Analyze Email

</button>

</form>

</div>

<button id="analyzeBtn" type="submit">

<span id="btnIcon">🚀</span>

<span id="btnText">

Analyze Email with Gemini AI

</span>

<div class="loader hidden"></div>

</button>

<section class="stats">

<div class="stat">

<h2>99%</h2>

<p>Detection Accuracy</p>

</div>

<div class="stat">

<h2>5000+</h2>

<p>Emails Tested</p>

</div>

<div class="stat">

<h2>24/7</h2>

<p>AI Monitoring</p>

</div>

<div class="stat">

<h2>Gemini</h2>

<p>AI Powered</p>

</div>

</section>

<section class="features">

<div class="feature">

<h3>🤖 AI Analysis</h3>

<p>

Gemini AI explains why an email is suspicious.

</p>

</div>

<div class="feature">

<h3>🌐 URL Scanner</h3>

<p>

Extracts every link and checks suspicious domains.

</p>

</div>

<div class="feature">

<h3>📊 Risk Score</h3>

<p>

Generates phishing probability and threat level.

</p>

</div>

<div class="feature">

<h3>📄 PDF Report</h3>

<p>

Download a professional security report.

</p>

</div>

<div class="feature">

<h3>📈 Analytics</h3>

<p>

Interactive dashboard with charts.

</p>

</div>

<div class="feature">

<h3>☁ Deploy Ready</h3>

<p>

GitHub + Render ready architecture.

</p>

</div>

</section>

<footer>

Made with ❤️ using Flask + Gemini AI + HTML + CSS + Javascript
    
</footer>

<script src="{{ url_for('static', filename='js/script.js') }}"></script>

</body>

</html>
