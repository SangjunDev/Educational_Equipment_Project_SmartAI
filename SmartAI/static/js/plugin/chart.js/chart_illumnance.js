let timeList = [];
let illumList = [];
var count =1;

$(document).ready(function(){ 

  getGraph();

});

function getGraph(){
      $.ajax({
          url:"/json/illumunance",
          type:"GET",
          dataType:"json",
          cache: false,
          success:function(data){

            timeList.push(data[0][3]);    				  
            illumList.push(data[0][2]);	

              if(count>8){ 
                timeList.shift();
                illumList.shift();
              }
              count++;	  

            setTimeout(getGraph, 5000);

            chart= new Chart(document.getElementById("line-chart").getContext('2d'), {
                type: 'line',
                data: {
                  labels: timeList,
                  datasets: [{ 
                      data: illumList, 
                      label: "Illuminance",
                      borderColor: 'rgb(75, 192, 192)',
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

                                 
          }
      }
      );  
  }; 
