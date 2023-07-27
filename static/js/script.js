const question = document.querySelector(".question");
const answers = document.querySelector(".answers");
const spnQtd = document.querySelector(".spnQtd");

import questions from "./questions.js";

let currentIndex = 0;
let answers2 = []

let usuario_id = document.getElementById("usuario_id").value;
let loading = document.querySelector(".loading-container");


function nextQuestion(e) {
  answers2.push(e.target.getAttribute("data-value"))

  if (currentIndex < questions.length - 1) {
    currentIndex++;
    loadQuestion();
  } else {
    finish();
    // getUsuario_id()
  }
}

function finish() {      
  const values = answers2;
  loading.style.display = 'block'
  // Enviar os valores selecionados para o Python
  fetch('/submit/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ values, usuario_id })
  })
  .then(response => response.json())
  .then(data => {
    const result = data.result; // Receber o resultado do Python
    window.location.href = `/resultado/${result}`; // Redirecionar para a página de resultado
  })
  .catch(error => {
    loading.style.display = 'none'
    alert('Erro: ' + error.message)
    console.error('Erro:', error);
  })
}


function loadQuestion() {
  console.log(currentIndex)
  console.log(currentIndex)
  if(currentIndex < questions.length){
    spnQtd.innerHTML = `${currentIndex + 1}/${questions.length}`;
    const item = questions[currentIndex];
    answers.innerHTML = "";
    question.innerHTML = item.question;


  
    item.answers.forEach((answer) => {
      const div = document.createElement("div");
      
      div.innerHTML = `
      <button class="answer" data-value="${answer.value}">
        ${answer.option}
      </button>
      `;

      answers.appendChild(div);
    });
  
  document.querySelectorAll(".answer").forEach((item) => {
    item.addEventListener("click", nextQuestion);
  });
  }
}
  loadQuestion();

