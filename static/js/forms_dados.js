function validarEmail(event) {
    var emailInput = document.getElementById("email");
    var email = emailInput.value;
    var allowedDomains = ["gmail.com", "outlook.com", "yahoo.com", "icloud.com", "hotmail.com", "aol.com", "protonmail.com", "mail.com", "zoho.com", "fastmail.com"];

    var emailDomain = email.split('@')[1];

    if (allowedDomains.indexOf(emailDomain) === -1) {
        alert("O domínio do e-mail não é permitido.");
        event.preventDefault();
        return false; // Impede o envio do formulário
    }

    return true; // Permite o envio do formulário
}