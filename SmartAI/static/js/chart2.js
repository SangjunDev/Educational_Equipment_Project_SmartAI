let timeList = [];
let posList = [];

function getGraph(){
      $.ajax({
          url:"/graph/live_gas",
          type:"get",
          dataType:"json",
          success:function(data){
              // console.log(data[0].pos_count);
              // 그래프로 나타낼 자료 리스트에 담기
              timeList.push(data[0][1]);    				  
              posList.push(data[0][0]);		  


            setTimeout(getGraph, 5000);

            chart= new Chart(document.getElementById("line-chart"), {
                type: 'line',
                data: {
                  labels: timeList, // X축 
                  datasets: [{ 
                      data: posList, // 값
                      label: "Illuminance",
                      borderColor: "#3e95cd",
                      fill: false
                    }
                  ]
                },
                options: {
                  title: {
                    display: true,
                    text: 'Sensor'
                  }
                }
              });

                                 
          },
          cache: false
      });  
  } // getGraph

function gclear(){
for(i=0 ; i<10; i++){
    timeList[i]=null;
    posList[i] = null;   
    }

chart.update();
chart.destory();

}      
  
$(document).ready(function(){ 

      getGraph();

});