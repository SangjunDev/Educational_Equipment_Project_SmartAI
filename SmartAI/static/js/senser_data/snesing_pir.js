
$(function pir() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/json/pir",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#pir_data").text(data[0][2]);
            }

        });

    }, 1000);

});