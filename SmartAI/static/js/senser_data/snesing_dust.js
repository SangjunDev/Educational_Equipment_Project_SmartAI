$(function gas() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_dust",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#dust_data").text(data);
            }

        });

    }, 5000);

});