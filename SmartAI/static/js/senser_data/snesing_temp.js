$(function temp() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_temp",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#temp_data").text(data);
            }

        });

    }, 5000);

});