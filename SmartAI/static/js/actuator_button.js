function led(element) {
    console.log(element.checked);

    if (element.checked == true){

        


    fetch("/led/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result_led");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Erro`r</h4>"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/led/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result_led");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Erraor</h4>"
                    }  
        });


    }
    
}

function fan(element) {
    console.log(element.checked);

    if (element.checked == true){

    fetch("/fan/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result_fan");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/fan/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result_fan");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });


    }
    
}

function solenoid(element) {
    console.log(element.checked);

    if (element.checked == true){

    fetch("/solenoid/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result_solenoid");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/solenoid/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result_solenoid");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });


    }
    
}

function doorlock(element) {
    console.log(element.checked);

    if (element.checked == true){

    fetch("/doorlock/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result_doorlock");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/doorlock/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#resul_doorlock");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });


    }
    
}

function button(element) {
    console.log(element.checked);

    if (element.checked == true){

    fetch("/button/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result_button");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/button/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result_button");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>"
                    }  
        });


    }
    
}