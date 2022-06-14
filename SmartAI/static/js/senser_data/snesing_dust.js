$(function gas() {

    timer = setInterval(function () {

        $.ajax({

            "url": "/api/dust",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#dust_data").text(data[0][2]);
            }

        });

    }, 1000);

});