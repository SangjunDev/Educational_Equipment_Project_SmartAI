$(function gas() {
    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_gas",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#gas_data").text(data[0][2]);

               
            }
            
        });
        
    },1000);



});