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
  for (var i=0; i<cols_list.length; i++) {
      console.log("in loop");
      //var opt = arr[i];
      //var el = document.createElement("option");
      //el.textContent = opt;
      //el.value = opt;
      //select.add(el);
  }​
}
