// from data.js
var tableData = data;

var tbody = d3.select("tbody");

function table(data) {
  tbody.html("");
  data.forEach((dataRow) => { var row = tbody.append("tr");
  Object.values(dataRow).forEach((val) => { var cell = row.append("td");
  cell.text(val);
  }
  );
  });
}

function update() {
  var date = d3.select("#datetime").property("value");
  let newdata = tableData;
  
  if (date) {
    newdata = newdata.filter(row => row.datetime === date);
  }
  table(newdata);
}

d3.selectAll("#filter-btn").on("click", update);

table(tableData);
