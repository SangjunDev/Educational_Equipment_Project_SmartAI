function led_on() {
    fetch("/led/on")
        .then(response => response.text())
        .then(data => {
          console.log(data);  
          let result = document.querySelector("#result");
          if (data == "OK") {
                      result.innerHTML = "<h6>ON</h6>";
                  }
          else {
                      result.innerHTML = "<h6>Error</h6>;"
                  }             
          
    });
}

function led_off() {
    fetch("/led/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result");
            if (data == "OK") {
                        result.innerHTML = "<h6>OFF</h6>";
                    }
            else {
                        result.innerHTML = "<h6>Error</h6>;"
                    }

        });
}
function led2_on() {
    fetch("/led2/on")
        .then(response => response.text())
        .then(data => {
          console.log(data);  
          let result = document.querySelector("#result2");
          if (data == "OK") {
                      result.innerHTML = "<h6>ON</h6>";
                  }
          else {
                      result.innerHTML = "<h6>Error</h6>;"
                  }          
    });
}

function led2_off() {
    fetch("/led2/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result2");
            if (data == "OK") {
                        result.innerHTML = "<h6>OFF</h6>";
                    }
            else {
                        result.innerHTML = "<h6>Error</h6>;"
                    }  
        });
}
function led3_on() {
    fetch("/led3/on")
        .then(response => response.text())
        .then(data => {
          console.log(data);  
          let result = document.querySelector("#result3");
          if (data == "OK") {
                      result.innerHTML = "<h6>ON</h6>";
                  }
          else {
                      result.innerHTML = "<h6>Error</h6>;"
                  }  
    });
}

function led3_off() {
    fetch("/led3/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result3");
            if (data == "OK") {
                        result.innerHTML = "<h6>OFF</h6>";
                    }
            else {
                        result.innerHTML = "<h6>Error</h6>;"
                    }  
        });
}
