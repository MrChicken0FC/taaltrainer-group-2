function controleer(goed, taal, level) {
    const feedback = document.getElementById("feedback");
    const volgendeKnop = document.getElementById("volgendeKnop");
    const opnieuwKnop = document.getElementById("opnieuwKnop");

    if (goed) {
        feedback.textContent = "✅ Antwoord goed!";
        feedback.style.color = "green";
        opnieuwKnop.style.display = "none";

        fetch("/api/complete_level", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ language: taal, level: level })
        }).then(() => {
            if (level === 6) {
                feedback.textContent = "🎉 Gefeliciteerd! Je hebt alle levels voltooid!";
                volgendeKnop.style.display = "none";
            } else {
                volgendeKnop.style.display = "inline";
            }
        });

    } else {
        feedback.textContent = "❌ Fout antwoord!";
        feedback.style.color = "red";
        volgendeKnop.style.display = "none";
        opnieuwKnop.style.display = "inline";
    }
}

function opnieuw() {
    document.getElementById("feedback").textContent = "";
    document.getElementById("volgendeKnop").style.display = "none";
    document.getElementById("opnieuwKnop").style.display = "none";
}