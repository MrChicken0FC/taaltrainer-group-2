let woordenMakkelijk = [
    { nl: "hond", en: "dog" },
    { nl: "kat", en: "cat" },
    { nl: "boek", en: "book" }
];

let woordenMoeilijk = [
    { nl: "ontwikkeling", en: "development" },
    { nl: "verantwoordelijkheid", en: "responsibility" },
    { nl: "maatschappij", en: "society" }
];

let woorden;
let huidigeVraag;
let score = 0;
let tijdOver = 10;
let timer;
let aantalVragen = 5;
let gespeeldeVragen = 0;

// Start spel
function startSpel() {
    const niveau = document.getElementById("niveau").value;
    woorden = niveau === "makkelijk" ? woordenMakkelijk : woordenMoeilijk;

    score = 0;
    gespeeldeVragen = 0;
    document.getElementById("score").textContent = score;
    document.getElementById("eindscherm").style.display = "none";

    nieuweVraag();
}

// Nieuwe vraag
function nieuweVraag() {
    if (gespeeldeVragen >= aantalVragen) {
        eindSpel();
        return;
    }

    gespeeldeVragen++;
    tijdOver = 10;
    document.getElementById("tijd").textContent = tijdOver;

    const randomIndex = Math.floor(Math.random() * woorden.length);
    huidigeVraag = woorden[randomIndex];

    document.getElementById("vraag").textContent = huidigeVraag.nl;
    document.getElementById("antwoord").value = "";
    document.getElementById("feedback").textContent = "";

    startTimer();
}

// Timer
function startTimer() {
    clearInterval(timer);

    timer = setInterval(() => {
        tijdOver--;
        document.getElementById("tijd").textContent = tijdOver;

        if (tijdOver <= 0) {
            clearInterval(timer);
            document.getElementById("feedback").textContent =
                "⏰ Tijd om! Antwoord was: " + huidigeVraag.en;
            setTimeout(nieuweVraag, 1500);
        }
    }, 1000);
}

// Controleer antwoord
function controleer() {
    clearInterval(timer);

    const userInput = document.getElementById("antwoord").value.toLowerCase();

    if (userInput === huidigeVraag.en) {
        score++;
        document.getElementById("feedback").textContent = "✅ Goed!";
    } else {
        document.getElementById("feedback").textContent =
            "❌ Fout! Het juiste antwoord is: " + huidigeVraag.en;
    }

    document.getElementById("score").textContent = score;

    setTimeout(nieuweVraag, 1500);
}

// Uitspraak (Web Speech API)
function spreekUit() {
    const speech = new SpeechSynthesisUtterance(huidigeVraag.en);
    speech.lang = "en-US";
    speechSynthesis.speak(speech);
}

// Eindscherm
function eindSpel() {
    document.getElementById("eindscherm").style.display = "block";
    document.getElementById("eindscore").textContent =
        "Je score is: " + score + " van de " + aantalVragen;

    localStorage.setItem("laatsteScore", score);
}

// Restart
function restart() {
    startSpel();
}

// Automatisch starten bij laden
window.onload = function () {
    const opgeslagenScore = localStorage.getItem("laatsteScore");
    if (opgeslagenScore !== null) {
        alert("Je laatste score was: " + opgeslagenScore);
    }
    startSpel();
};
const API_KEY = "ta_1410a8f23";