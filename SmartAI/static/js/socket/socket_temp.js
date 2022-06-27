const temp = [];
const humi = [];
const time = [];
var count =1;


$(document).ready(function(){
    console.log('http://' + document.domain + ':' + location.port + '/sockettest')


    var socket = io.connect('http://' + document.domain + ':' + location.port + '/sockettest') ;
   
    socket.on('connect', function(msg){
            var connect_string = 'connect';
            console.log(connect_string)
            socket.emit('request', connect_string);
    });

    socket.on('response', function(msg){
            if(msg.type === 'data'){
                    $('#messages_1').text(msg.temp);
                    $('#messages_2').text(msg.humi);
                    temp.push(msg.temp);
                    humi.push(msg.humi);
                    time.push(msg.time);
                    getGraph(temp, humi, time);
                    

            }else{
                    $('#messages').text('error');
            }
            console.log('Received Message : '+msg.type);



            
    });

    socket.on('disconnect', function(msg){image.png
      var connect_string = 'disconnect';
      console.log(connect_string)
});image.png


});
    




function getGraph(data1, data2, data3){

      chart= new Chart(document.getElementById("line-chart"), {
        type: 'line',
                    data: {
                      labels: data3,
                      datasets: [{ 
                          data: data1, 
                          label: "Temp",
                          borderColor: 'rgb(75, 192, 192)',
                          fill: false,
                          borderWidth: 2
                        },{ 
                          data: data2, 
                          label: "Humi",
                          borderColor: 'rgb(0, 255, 255)',
                          fill: false,
                          borderWidth: 2
                        }
    
                      ]
                    },
                    options: {
                      responseive: false,
                      title: {
                        display: true,
                        text: 'Sensor'
                      }
                    }


      });


      if(count>8){ 
        data1.shift();
        data2.shift();
        data3.shift();
      }
      count++;
                       
              };  
      