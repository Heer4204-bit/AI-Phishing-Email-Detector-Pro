<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Phishing Email Detector 📧</title>
  <style>
    :root {
      --bg-color: #0f172a;
      --card-bg: #1e293b;
      --text-color: #f8fafc;
      --accent-color: #3b82f6;
      --accent-hover: #2563eb;
      --safe-color: #22c55e;
      --danger-color: #ef4444;
      --border-color: #334155;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-color);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
      box-sizing: border-box;
    }

    .container {
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 30px;
      max-width: 650px;
      width: 100%;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }

    h1 {
      font-size: 1.5rem;
      margin-top: 0;
      margin-bottom: 20px;
      text-align: center;
    }

    label {
      display: block;
      font-size: 0.9rem;
      font-weight: 600;
      margin-bottom: 8px;
    }

    textarea {
      width: 100%;
      height: 160px;
      background-color: #0f172a;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-color);
      padding: 12px;
      font-size: 0.95rem;
      resize: vertical;
      box-sizing: border-box;
      margin-bottom: 20px;
    }

    textarea:focus {
      outline: 2px solid var(--accent-color);
      border-color: transparent;
    }

    button {
      width: 100%;
      background-color: var(--accent-color);
      color: white;
      border: none;
      padding: 12px;
      font-size: 1rem;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.2s ease;
    }

    button:hover {
      background-color: var(--accent-hover);
    }

    .result-card {
      margin-top: 20px;
      padding: 15px;
      border-radius: 8px;
      display: none;
      border: 1px solid transparent;
    }

    .result-card.safe {
      background-color: rgba(34, 197, 94, 0.1);
      border-color: var(--safe-color);
      color: var(--safe-color);
    }

    .result-card.danger {
      background-color: rgba(239, 68, 68, 0.1);
      border-color: var(--danger-color);
      color: var(--danger-color);
    }

    .result-title {
      font-weight: bold;
      font-size: 1.1rem;
      margin-bottom: 5px;
    }

    .result-details {
      color: var(--text-color);
      font-size: 0.9rem;
      margin-top: 8px;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>AI Phishing Email Detector Pro 📧</h1>
    
    <label for="emailInput">Paste Email Content Below:</label>
    <textarea id="emailInput" placeholder="Dear user, your account has been suspended. Click here to verify..."></textarea>
    
    <button onclick="analyzeEmail()">Analyze Email</button>

    <div id="result" class="result-card">
      <div id="resultTitle" class="result-title"></div>
      <div id="resultDetails" class="result-details"></div>
    </div>
  </div>

  <script>
    function analyzeEmail() {
      const input = document.getElementById("emailInput").value.toLowerCase();
      const resultDiv = document.getElementById("result");
      const titleDiv = document.getElementById("resultTitle");
      const detailsDiv = document.getElementById("resultDetails");

      if (!input.trim()) {
        alert("Please paste email content to analyze.");
        return;
      }

      // Keyword heuristic trigger list
      const suspiciousKeywords = [
        "urgent", "verify your account", "suspended", "password reset", 
        "click here", "bank", "unauthorized", "social security", 
        "lottery", "prize", "action required", "immediate"
      ];

      let detectedKeywords = [];
      suspiciousKeywords.forEach(word => {
        if (input.includes(word)) {
          detectedKeywords.push(word);
        }
      });

      resultDiv.style.display = "block";

      if (detectedKeywords.length > 0) {
        resultDiv.className = "result-card danger";
        titleDiv.textContent = "⚠️ Potential Phishing Attempt Detected!";
        detailsDiv.innerHTML = `This email contains high-risk keywords: <strong>${detectedKeywords.join(", ")}</strong>. Avoid clicking any links or sharing sensitive personal data.`;
      } else {
        resultDiv.className = "result-card safe";
        titleDiv.textContent = "✅ Looks Safe";
        detailsDiv.textContent = "No common phishing triggers were detected in this email text. Always double-check sender details manually.";
      }
    }
  </script>

</body>
</html>
