const recBtn = document.getElementById("recBtn");
const stopBtn = document.getElementById("stopBtn");
const ul = document.getElementById("sttResult");

recBtn.addEventListener("click", () =>{


    annyang.setLanguage('ko');
  
    annyang.start({ autoRestart: false, continuous: false });
  
    const recognition = annyang.getSpeechRecognizer();
  
    let final_transcript = "";
  
    recognition.interimResults = true;
  
    recognition.onresult = function (event) {
      console.log(event);
  
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          final_transcript += event.results[i][0].transcript;
          console.log("final_transcript=" + final_transcript);
          if (final_transcript =='LED 꺼'){
                fetch("/led/off")
                    .then(response => response.text())
                    .then(data => {console.log(data);});
          } else if(final_transcript == 'LED 켜'){
            fetch("/led/on")
            .then(response => response.text())
            .then(data => {console.log(data);});
          }
  
          const html = `<li>${final_transcript}</li>`;
  
          ul.insertAdjacentHTML("beforeend", html);
        } else {
        }
      }
  
    };




});
stopBtn.addEventListener("click", ()=>{
    annyang.abort();
});


