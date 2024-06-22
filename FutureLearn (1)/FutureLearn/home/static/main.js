// Function to redirect to the form page
function redirectToForm() {
    window.location.href = 'registration.html';
}

// Questions array
const Questions = [{
    q: "What is language of web development?",
    a: [{ text: "DBMS", isCorrect: false },
        { text: "C++", isCorrect: false },
        { text: "HTML-CSS", isCorrect: true },
        { text: "Data science", isCorrect: false }
    ]
},
{
    q: "Which is related to Chat-GPT?",
    a: [{ text: "Block-chain", isCorrect: false },
        { text: "Python", isCorrect: false },
        { text: "Artificial-intelligence", isCorrect: true },
        { text: "Data structures", isCorrect: false }
    ]
},
{
    q: "Which of the following is a frontend framework?",
    a: [{ text: "React", isCorrect: true },
        { text: "Django", isCorrect: false },
        { text: "Flask", isCorrect: false },
        { text: "TensorFlow", isCorrect: false }
    ]
},
{
    q: "Which language is primarily used for developing Android applications?",
    a: [{ text: "Swift", isCorrect: false },
        { text: "Java", isCorrect: true },
        { text: "C#", isCorrect: false },
        { text: "Ruby", isCorrect: false }
    ]
},
{
    q: "Which HTTP method is used to update resources on a web server?",
    a: [{ text: "GET", isCorrect: false },
        { text: "POST", isCorrect: false },
        { text: "PUT", isCorrect: true },
        { text: "DELETE", isCorrect: false }
    ]
}];

let currQuestion = 0;
let score = 0;

// Function to load the current question and its options
function loadQues() {
    const question = document.getElementById("ques");
    const opt = document.getElementById("opt");

    question.textContent = Questions[currQuestion].q;
    opt.innerHTML = "";

    for (let i = 0; i < Questions[currQuestion].a.length; i++) {
        const choicesdiv = document.createElement("div");
        const choice = document.createElement("input");
        const choiceLabel = document.createElement("label");

        choice.type = "radio";
        choice.name = "answer";
        choice.value = i;

        choiceLabel.textContent = Questions[currQuestion].a[i].text;

        choicesdiv.appendChild(choice);
        choicesdiv.appendChild(choiceLabel);
        opt.appendChild(choicesdiv);
    }
}

loadQues();

// Function to display the score
function loadScore() {
    const totalScore = document.getElementById("score");
    totalScore.textContent = `You scored ${score} out of ${Questions.length}`;
}

// Function to load the next question or display the score if it's the last question
function nextQuestion() {
    if (currQuestion < Questions.length - 1) {
        currQuestion++;
        loadQues();
    } else {
        document.getElementById("opt").remove();
        document.getElementById("ques").remove();
        document.getElementById("btn").remove();
        loadScore();
    }
}

// Function to check the selected answer
function checkAns() {
    const selectedAns = parseInt(document.querySelector('input[name="answer"]:checked').value);

    if (Questions[currQuestion].a[selectedAns].isCorrect) {
        score++;
        console.log("Correct");
    }
    nextQuestion();
}




