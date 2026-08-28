const analyzeBtn = document.getElementById("analyzeBtn");
const urlInput = document.getElementById("urlInput");

urlInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {

        event.preventDefault();

        analyzeBtn.click();

    }

});

analyzeBtn.addEventListener("click", analyzeURL);

loadStatistics();
loadHistory();

async function analyzeURL() {

    const url = document.getElementById("urlInput").value.trim();

    if (url === "") {
        alert("Please enter a URL.");
        return;
    }

    analyzeBtn.disabled = true;

    analyzeBtn.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        Analyzing...
    `;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: url
                })
            }
        );

        console.log("Status:", response.status);

        const data = await response.json();

        console.log("Backend Response:", data);

        if (!response.ok) {

            throw new Error(JSON.stringify(data));

        }

        updateResult(data);

    }

    catch (error) {

        console.error("Actual Error:", error);

        alert(error.message);

    }

    finally {

        analyzeBtn.disabled = false;

        analyzeBtn.innerHTML = `
            <i class="fa-solid fa-magnifying-glass"></i>
            Analyze
        `;

    }

}



function updateResult(data) {

    document
        .getElementById("resultSection")
        .classList
        .remove("hidden");

    const verdict =
        document.getElementById("verdictText");

    const verdictDescription =
        document.getElementById("verdictDescription");

    verdict.classList.remove(
        "safe",
        "suspicious",
        "phishing"
    );

    if (data.verdict === "Safe") {

        verdict.classList.add("safe");

        verdict.innerHTML = "🟢 Safe";

        verdictDescription.innerHTML =
            "This website appears to be safe.";

    }

    else if (data.verdict === "Suspicious") {

        verdict.classList.add("suspicious");

        verdict.innerHTML = "🟡 Suspicious";

        verdictDescription.innerHTML =
            "This URL requires manual verification.";

    }

    else {

        verdict.classList.add("phishing");

        verdict.innerHTML = "🔴 Phishing";

        verdictDescription.innerHTML =
            "This website is highly dangerous.";

    }

    document.getElementById("riskScore").innerHTML =
        data.risk_score;

    document.getElementById("domainValue").innerHTML =
        data.url_details.domain;

    document.getElementById("httpsValue").innerHTML =
        data.https_enabled ? "Yes" : "No";

    document.getElementById("lengthValue").innerHTML =
        data.url_length;

    document.getElementById("maliciousValue").innerHTML =
        data.virustotal.malicious;

    document.getElementById("suspiciousValue").innerHTML =
        data.virustotal.suspicious;

    document.getElementById("harmlessValue").innerHTML =
        data.virustotal.harmless;

    document.getElementById("undetectedValue").innerHTML =
        data.virustotal.undetected;

    loadStatistics();

    loadHistory();

}

async function loadStatistics() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/history"
        );

        const scans = await response.json();

        document.getElementById("totalScans").innerHTML =
            scans.length;

        let safe = 0;
        let threats = 0;

        scans.forEach(scan => {

            if (scan.verdict === "Safe") {

                safe++;

            }

            else {

                threats++;

            }

        });

        document.getElementById("safeLinks").innerHTML =
            safe;

        document.getElementById("threatLinks").innerHTML =
            threats;

    }

    catch (error) {

        console.error("Statistics Error:", error);

    }

}

async function loadHistory() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/history"
        );

        const scans = await response.json();

        const historyBody =
            document.getElementById("historyBody");

        historyBody.innerHTML = "";

        scans.forEach(scan => {

            historyBody.innerHTML += `

            <tr>

                <td>${scan.id}</td>

                <td>${scan.domain}</td>

                <td>${scan.verdict}</td>

                <td>${scan.risk_score}</td>

                <td>${new Date(scan.created_at).toLocaleString()}</td>

                <td>

                    <button
                        class="deleteBtn"
                        onclick="deleteScan(${scan.id})">

                        Delete

                    </button>

                </td>

            </tr>

            `;

        });

    }

    catch (error) {

        console.error(error);

    }

}



async function deleteScan(id) {

    if (!confirm("Delete this scan?")) {

        return;

    }

    await fetch(
        `http://127.0.0.1:8000/history/${id}`,
        {
            method: "DELETE"
        }
    );

    loadHistory();

    loadStatistics();

}

