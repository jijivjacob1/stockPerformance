
 var $outcome = document.querySelector(".displayResult");

// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  Plotly.d3.event.preventDefault();

  // Select the input value from the form
  var stock = Plotly.d3.select("#stockInput").node().value;
  console.log(stock);

  // clear the input value
  Plotly.d3.select("#stockInput").node().value = "";

  // Build the plot with the new stock
  // buildPlot(stock);
  // console.log("hello");
  Plotly.d3.json("/predictStock/" + stock, function(error, response) {
    if (error) return console.warn(error);

    //console.log(response);

  if (response.length > 0){

    price_change = response.map(d=>d.price_change);
    sp_price_change = response.map(d=>d.sp_price_change);
    sp_dates = response.map(d=>d.datekey);
    statuses = response.map(d=>d.status);
    //console.log(price_change);
    //console.log(sp_price_change);
    //console.log(sp_dates);

    var layout = {
      title: '',
      xaxis: {
        title: 'Years'
      },
      yaxis: {
        title: 'Price Change'
      }
    };
    

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: stock ,
      x: sp_dates,
      y: price_change,
      line: {color: '#17BECF'}
    }
    
    var trace2 = {
      type: "scatter",
      mode: "lines",
      name: 'S&P',
      x: sp_dates,
      y: sp_price_change,
      line: {color: '#7F7F7F'}
    }
    
    var data = [trace1,trace2];
    
   
    
    Plotly.newPlot('plot', data,layout);

   
    $outcome.innerHTML = statuses[0]

    var $tbody = document.querySelector(".features");

    $tbody.innerHTML = "";
    for (var i = 0; (i < (response.length)) ; i++) {
      var stkdata = response[i];
      var $row = $tbody.insertRow(i);

      for (var j = 0; j < 10; j++) {
        var $cell = $row.insertCell(j);


       if (j == 0){
          $cell.innerText = stkdata["pb"];
        }
        if (j == 1){
          $cell.innerText = stkdata["pe1"];
        }
        if (j == 2){
          $cell.innerText = stkdata["tangibles"];
        }
        if (j == 3){
          $cell.innerText = stkdata["sps"];
        }
        if (j == 4){
          $cell.innerText = stkdata["ps1"];
        }
        if (j == 5){
          $cell.innerText = stkdata["debtusd"];
        }
        if (j == 6){
          $cell.innerText = stkdata["evebitda"];
        }
        if (j == 7){
          $cell.innerText = stkdata["depamor"];
        }
        if (j == 8){
          $cell.innerText = stkdata["epsdil"];
        }
        if (j == 9){
          $cell.innerText = stkdata["de"];
        }

      
      }

    }
  }
  else
  {
    $outcome.innerHTML =  "Data Unavailable"
  }
    
      

})
}



// Add event listener for submit button
Plotly.d3.select("#submit").on("click", handleSubmit);
