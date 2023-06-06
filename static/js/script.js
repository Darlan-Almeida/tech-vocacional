const question = document.querySelector(".question");
const answers = document.querySelector(".answers");
const spnQtd = document.querySelector(".spnQtd");
const textFinish = document.querySelector(".finish span");
const content = document.querySelector(".content");
const contentFinish = document.querySelector(".finish");

import questions from "./questions.js";

let currentIndex = 0;
let answers2 = []

function nextQuestion(e) {
  answers2.push(e.target.getAttribute("data-value"))

  if (currentIndex < questions.length - 1) {
    currentIndex++;
    loadQuestion();
  } else {
    finish();
  }
}

function finish() {
  textFinish.innerHTML = "Parabéns, você concluiu o questionário!";
  content.style.display = "none";
  contentFinish.style.display = "block";
      
  const values = answers2;
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/submit", true);
  xhr.setRequestHeader("Content-Type", "application/json"); 
  // Enviar o objeto JSON com os valores das questões
  xhr.send(JSON.stringify({ values }));
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

