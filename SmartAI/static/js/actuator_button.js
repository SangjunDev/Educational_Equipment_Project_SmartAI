function led_2(element) {
    console.log(element.checked);

    if (element.checked == true){

    fetch("/led2/on")
    .then(response => response.text())
    .then(data => {
      console.log(data);  
      let result = document.querySelector("#result2");
            if (data == "OK") {
                        result.innerHTML = "<h4 >ON</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>;"
                    }  
        });
    }
    else if(element.checked == false) {
        fetch("/led2/off")
        .then(response => response.text())
        .then(data => {
            console.log(data);
            let result = document.querySelector("#result2");
            if (data == "OK") {
                        result.innerHTML = "<h4>OFF</h4>";
                    }
            else {
                        result.innerHTML = "<h4>Error</h4>;"
                    }  
        });


    }
    
}