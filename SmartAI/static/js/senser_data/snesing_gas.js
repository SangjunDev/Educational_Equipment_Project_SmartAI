$(function gas() {

        $.ajax({

            "url": "/sensor/live_gas",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#gas_data").text(data);

                setTimeout(gas, 5000);
            }, 
            cache: false
            
        }
        );



});