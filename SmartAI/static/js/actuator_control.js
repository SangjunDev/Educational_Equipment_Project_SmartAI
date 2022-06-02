function led_on() {
    fetch("/led/on")
        .then(response => response.json())
        .then(data => {
          console.log(data);  
    });
}

function led_off() {
    fetch("/led/off")
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}
function led2_on() {
    fetch("/led2/on")
        .then(response => response.json())
        .then(data => {
          console.log(data);  
    });
}

function led2_off() {
    fetch("/led2/off")
        .then(response => response.jsont())
        .then(data => {
            console.log(data);
        });
}
function led3_on() {
    fetch("/led3/on")
        .then(response => response.json())
        .then(data => {
          console.log(data);  
    });
}

function led3_off() {
    fetch("/led3/off")
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}
