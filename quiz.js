(function(){
 
  function buildQuiz(){
  
    const output = [];


    myQuestions.forEach(
      (currentQuestion, questionNumber) => {

    
        const answers = [];

       
        for(letter in currentQuestion.answers){

   
          answers.push(
            `<label>
              <input type="radio" name="question${questionNumber}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
          );
        }

       
        output.push(
          `<div class="slide">
            <div class="question"> ${currentQuestion.question} </div>
            <div class="answers"> ${answers.join("")} </div>
          </div>`
        );
      }
    );

   
    quizContainer.innerHTML = output.join('');
  }

  function showResults(){


    const answerContainers = quizContainer.querySelectorAll('.answers');

   
    let numCorrect = 0;

 
    myQuestions.forEach( (currentQuestion, questionNumber) => {

   
      const answerContainer = answerContainers[questionNumber];
      const selector = `input[name=question${questionNumber}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;

    
      if(userAnswer === currentQuestion.correctAnswer){
     
        numCorrect++;

       
        answerContainers[questionNumber].style.color = 'lightgreen';
      }
    
      else{
       
        answerContainers[questionNumber].style.color = 'red';
      }
    });

  
    resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
  }

  function showSlide(n) {
    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    if(currentSlide === 0){
      previousButton.style.display = 'none';
    }
    else{
      previousButton.style.display = 'inline-block';
    }
    if(currentSlide === slides.length-1){
      nextButton.style.display = 'none';
      submitButton.style.display = 'inline-block';
    }
    else{
      nextButton.style.display = 'inline-block';
      submitButton.style.display = 'none';
    }
  }

  

  
  const quizContainer = document.getElementById('quiz');
  const resultsContainer = document.getElementById('results');
  const submitButton = document.getElementById('submit');
  const myQuestions = [
    {
      question: "A unlocked lock implies that:",
      answers: {
        a: "No thread is holding the lock.",
        b: "There is a thread holding the lock.",
        c: "There is no lock in place."
      },
      correctAnswer: "a"
    },
    {
      question: "What makes a data structure ‘thread safe’?",
      answers: {
        a: "When it allows data races",
        b: "When a data structure has a lock added",
        c: "When a data structure does not have a lock",
        d: "When a data structure has no threads"
      },
      correctAnswer: "b"
    },
    {
      question: "What are the operations associated with condition variables?",
      answers: {
        a: "Await()",
        b: "Lock()",
        c: "Signal()"
      },
      correctAnswer: "a"
    },
    {
      question: "What is one disadvantage with using an interrupt control?",
      answers: {
        a: "It requires a lot of memory and is inefficient",
        b: "It does not work on multiple processors.",
        c: "It is a slow process that takes long",
        d: "It is prone to bugs and errors"
      },
      correctAnswer: "b"
    },
    {
      question: "What is perfect scaling?",
      answers: {
        a: "Threads working solely",
        b: "Threads working in parallel",
        c: "Having optimal performance efficiency",
        d: "When a data structure is thread safe"
      },
      correctAnswer: "b"
    },
    {
      question: "When can a lock be released?",
      answers: {
        a: "When the Signal() condition has been met",
        b: "When the thread has been put to sleep",
        c: "When the thread has woken up"
      },
      correctAnswer: "b"
    },
    {
      question: "What is a disadvantage of using a concurrent approximate counter?",
      answers: {
        a: "The counter is can be inaccurate",
        b: "Cannot count large amounts of events",
        c: "It causes bugs in counter scalability on multicore machines",
        d: "Uses a large amount of memory"
      },
      correctAnswer: "a"
    },
    {
      question: "What are the criteria that a lock has to meet in order to evaluate its effectiveness? ",
      answers: {
        a: "Fairness: does each thread contending for the lock get a fair shot at acquiring it once it is free?",
        b: "Safety: does the lock run smoothly, without bugs?",
        c: "Does the lock allow for multicore processing?"
      },
      correctAnswer: "a"
    },
    {
      question: "What are the solutions to the spin lock problem?",
      answers: {
        a: "Unlock()",
        b: "Yield()",
        c: "Wait()",
        d: "Lock()"
      },
      correctAnswer: "b"
    },
    {
      question: "What is the purpose of the mutex system in the wait() operation?",
      answers: {
        a: "To stop Signal() if it has been called without the condition being met",
        b: "To ensure that Signal() is not called before Wait()",
        c: "To prevent race conditions from occurring"
      },
      correctAnswer: "c"
    }
  ];


  buildQuiz();


  const previousButton = document.getElementById("previous");
  const nextButton = document.getElementById("next");
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 9;


  showSlide(currentSlide);


  submitButton.addEventListener('click', showResults);
  
})();
