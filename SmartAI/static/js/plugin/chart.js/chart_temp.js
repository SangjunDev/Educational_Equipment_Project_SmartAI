let timeList = [];
let tempList_t = [];
let tempList_h = [];
var count =1;

$(document).ready(function(){ 

  getGraph();

});

function getGraph(){
      $.ajax({
          url:"/api/temp",
          type:"GET",
          dataType:"json",
          cache: false,
          success:function(data){

            timeList.push(data[0][4]);    				  
            tempList_t.push(data[0][2]);
            tempList_h.push(data[0][3]);		

              if(count>8){ 
                timeList.shift();
                tempList_t.shift();
                tempList_h.shift();
              }
              count++;	  

            setTimeout(getGraph, 5000);

            chart= new Chart(document.getElementById("line-chart").getContext('2d'), {
                type: 'line',
                data: {
                  labels: timeList,
                  datasets: [{ 
                      data: tempList_t, 
                      label: "Temp",
                      borderColor: 'rgb(75, 192, 192)',
                      fill: false,
                      borderWidth: 2
                    },{ 
                      data: tempList_h, 
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

                                 
          }
      }
      );  
  }; 
