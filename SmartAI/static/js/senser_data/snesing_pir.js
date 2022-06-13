
$(function pir() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_pir",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#pir_data").text(data);
            }

        });

    }, 5000);

});