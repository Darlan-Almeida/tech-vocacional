const question = document.querySelector(".question");
const answers = document.querySelector(".answers");
const spnQtd = document.querySelector(".spnQtd");
const textFinish = document.querySelector(".finish span");
const content = document.querySelector(".content");
const contentFinish = document.querySelector(".finish");
const btnRestart = document.querySelector(".finish button");

import questions from "./questions.js";

let currentIndex = 0;
let questionsCorrect = 0;
let answers2 = []

btnRestart.onclick = () => {
  content.style.display = "flex";
  contentFinish.style.display = "none";

  currentIndex = 0;
  questionsCorrect = 0;
  loadQuestion();
};

function nextQuestion(e) {
  // if (e.target.getAttribute("data-value") === "true") {
    // questionsCorrect++;
  // }
  answers2.push(e.target.getAttribute("data-value"))

  if (currentIndex < questions.length - 1) {
    currentIndex++;
    loadQuestion();
  } else {
    finish();
  }
}

function finish() {
  const values = answers2;
  // for (let i = 0; i < questions.length; i++) {
  //   const selectedOption = document.querySelector(`span[class="question${i}"]:checked`);
  //   console.log(selectedOption)
  //   if (selectedOption) {
  //     const value = selectedOption.value;
  //     const keyword = options[i].find(option => option.option === value).value;
  //     values.push(keyword);
  //   }
  // }

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/submit", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      const questionsCorrect = response.questionsCorrect;
      const totalQuestions = response.totalQuestions;

      const textFinish = document.getElementById("text-finish");
      textFinish.innerHTML = `Você acertou ${questionsCorrect} de ${totalQuestions}`;

      const content = document.getElementById("content");
      const contentFinish = document.getElementById("content-finish");
      content.style.display = "none";
      contentFinish.style.display = "flex";
    }
  };
  
  // Enviar o objeto JSON com os valores das questões
  xhr.send(JSON.stringify({ values }));
}

function loadQuestion() {
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

loadQuestion();