function getPathToFile() {
  console.log("just got to getPathToFile");
  eel.get_csv()(setScreen);
}

function sendCsvToPython() {
  var input = document.getElementById("input").value;
  eel.initialize_clemen(input)(setScreen);
}

function setScreen(cols_list){
  var arr = cols_list;
  console.log("just got to setScreen");
  console.log(arr.length)
  //var i;
  var select = document.getElementById("column");
  for (let step = 0; step < cols_list.length; step++) {
    // Runs 5 times, with values of step 0 through 4.
    console.log("in loop");
    var opt = arr[step];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.add(el);
  }
  //for (var i=0; i<cols_list.length; i++) {
  //
  //}​
}
