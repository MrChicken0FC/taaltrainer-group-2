// login dingus om data te senden naar python door de api te pakken
const loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", function(e) {
        e.preventDefault();

        fetch("/api/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: document.getElementById("email").value,
                password: document.getElementById("password").value
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                window.location.href = "/main";  
            } else {
                alert("Foute login!");
            }
        });
    });
}

// regristeren 
const registerForm = document.getElementById("registerForm");
if (registerForm) {
    registerForm.addEventListener("submit", function(e) {
        e.preventDefault();

        fetch("/api/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: document.getElementById("email").value,
                password: document.getElementById("password").value
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                alert("Account aangemaakt!");
                window.location.href = "/login";
            } else {
                alert("Account bestaat al!");
            }
        });
    });
}