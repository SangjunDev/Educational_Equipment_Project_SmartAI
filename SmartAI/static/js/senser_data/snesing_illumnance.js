$(function illuminance() {  
    timer = setInterval(function () { 

        $.ajax({

            "url": "/json/illumunance",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#illuminance_data").text(data[0][2]);

                
                
            }

        });

    },1000);
    

});







