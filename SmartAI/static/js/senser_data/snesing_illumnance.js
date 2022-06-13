$(function illuminance() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_illumunance",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#illuminance_data").text(data);
            }

        });

    }, 5000);

});







