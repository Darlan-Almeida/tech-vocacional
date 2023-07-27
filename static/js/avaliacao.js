var btn1 = document.querySelector('#green');
var btn2 = document.querySelector('#red');
var clicado = false;
var opiniao = null;

function myFunctionRed() {
  if (!clicado) {
    btn1.classList.remove('green');
    btn1.onclick = null; // Remove o evento de clique do botão vermelho
    btn2.classList.toggle('red');
    clicado = true;
    opiniao = "dislike"; // Inverte para "dislike" quando o botão vermelho é clicado
    mostrarOpiniao();
  }
}

function myFunctionGreen() {
  if (!clicado) {
    btn2.classList.remove('red');
    btn2.onclick = null; // Remove o evento de clique do botão verde
    btn1.classList.toggle('green');
    clicado = true;
    opiniao = "like"; // Inverte para "like" quando o botão verde é clicado
    mostrarOpiniao();
  }
}

function mostrarOpiniao() {
  console.log(opiniao)
}