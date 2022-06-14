$(function illuminance() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/api/illumunance",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#illuminance_data").text(data[0][2]);
            }

        });

    }, 5000);

});







