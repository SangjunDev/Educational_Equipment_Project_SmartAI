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

$(function gas() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/sensor/live_gas",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#gas_data").text(data);
            }

        });

    }, 5000);

});

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

$(function dust() {

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
