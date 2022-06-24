let messages_1 = [];
let messages_2 = [];
let messages_3 = [];
var count =1;


$(document).ready(function(){
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  console.log('http://' + document.domain + ':' + location.port)

  socket.on('connect', function(msg){
          var connect_string = 'connect';
          console.log('connect')
          socket.emit('server_temp', connect_string);
  });

  socket.on('client_1', function(msg){
          if(msg.type === 'data'){
                  $('#messages_1').text(msg.temp);
                  $('#messages_2').text(msg.humi);
                  $('#messages_3').text(msg.humi);
          }else{
                  $('#messages').text('error');
          }
          console.log('Received Message : '+msg.type);
  });

  getGraph(messages_1,messages_2,messages_3);
});

function getGraph(data1, data2, data3){
     	

/*
              if(count>8){ 
                data1.shift();
                data2.shift();
                data3.shift();
              }
              count++;	  
*/

            chart= new Chart(document.getElementById("line-chart").getContext('2d'), {
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
                  },
                  animation:{
                    animateScale: true,
                    animateRotate: true
                  }
                }
              });

                                 
          };


