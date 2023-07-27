var btn1 = document.querySelector('#green');
var btn2 = document.querySelector('#red');
var clicado = false;
var opiniao = null;

function myFunctionRed() {
  if (!clicado) {
    btn1.classList.remove('green');
    btn1.onclick = null; 
    btn2.classList.toggle('red');
    clicado = true;
    opiniao = "dislike"; 
    mostrarOpiniao();
  }
}

function myFunctionGreen() {
  if (!clicado) {
    btn2.classList.remove('red');
    btn2.onclick = null; 
    btn1.classList.toggle('green');
    clicado = true;
    opiniao = "like"; 
    mostrarOpiniao();
  }
}

function mostrarOpiniao() {
  console.log(opiniao)
}
