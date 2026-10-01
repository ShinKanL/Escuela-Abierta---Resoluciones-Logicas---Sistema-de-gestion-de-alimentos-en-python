function abrirLogin() {
    document.getElementById("fondo-login").classList.add("activo");
}
function cerrarLogin() {
    document.getElementById("fondo-login").classList.remove("activo");
}

function iniciarSesion() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (email === "" || password === "") {
        alert("Completá todos los campos.");
        return;
    }

    localStorage.setItem("email", email);
    localStorage.setItem("password", password);

    alert("¡Inicio de sesión guardado!");
    cerrarLogin();
}