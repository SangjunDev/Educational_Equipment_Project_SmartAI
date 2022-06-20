$(function temp() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/json/temp",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#temp_data").text(data[0][2]);
                $("#humi_data").text(data[0][3]);
                
            }

        });

    }, 1000);

});