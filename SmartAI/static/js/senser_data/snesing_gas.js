$(function gas() {

        $.ajax({

            "url": "/api/gas",
            type:"GET",
            dataType:"json",
            cache: false,
            success: function (data) {
                console.log(data);
                $("#gas_data").text(data[0][2]);

                setTimeout(gas, 1000);
            }, 
            cache: false
            
        }
        );



});