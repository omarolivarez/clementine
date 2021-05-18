function getPathToFile() {
  console.log("just got to getPathToFile");
  eel.get_csv()(setScreen);
}

/*function sendCsvToPython() {
  var input = document.getElementById("input").value;
  eel.initialize_clemen(input)(setScreen);
}*/

function setScreen(cols_list){
  var arr = cols_list;
  console.log("just got to setScreen");
  console.log(arr.length)
  var select = document.getElementById("column");
  for (let step = 0; step < cols_list.length; step++) {
    var opt = arr[step];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.add(el);
  }
}

function hideUnhide(form) {
  console.log("just got to hideUnhide");
  var col = form.column.value;
  var stat = form.statistic.value;
  var reps = form.repititions.value;
  var com = form.completed.value;
  console.log(stat);
  console.log(reps);
  var inElement = document.getElementById("input");
  inElement.style.display = "none";
  var formElement = document.getElementById("firstPageForm");
  formElement.style.display = "none";

  var pauseElement = document.getElementById("pause");
  pauseElement.style.display = "block";
  var progressElement = document.getElementById("progress");
  progressElement.style.display = "block";
  //progressElement.style.backgroundColor = "none";
  var progressDivElement = document.getElementById("progressDiv");
  progressDivElement.style.display = "block";
  progressDivElement.style.backgroundColor = "white";
  eel.bootstrap(col, stat, reps, com)();

}

function testResults (form) {
            var TestVar = form.inputbox.value;
            alert ("You typed: " + TestVar);
        }

function updateProgressAndCallSample(perc) {
  console.log("inside updateProgressAndCallSample()")
  console.log(perc)
  var progress = document.getElementById("progress");
  progress.style.width = perc;
  progress.innerHTML = perc;
  eel.sample();
}
eel.expose(updateProgressAndCallSample)

function endProgress(){
  
}
