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

var input = {};

function update() {
  var infotype = d3.select(this).select("input");
  var info = infotype.property("value");
  var index = infotype.attr("id");

  if (info) {
    input[index] = info;
  }

  else {
    delete input[index];
  }

  newtable();
}

function newtable() {
  let newdata = tableData;
  Object.entries(input).forEach(([key, value]) => { newdata = newdata.filter(row => row[key] === value);
  });
  table(newdata);
}

d3.selectAll(".filter").on("change", update);

table(tableData);
