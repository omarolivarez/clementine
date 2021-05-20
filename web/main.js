var clicked = false;
var p = document.getElementById("pause");
var radioButton = document.getElementById("gridRadios1")
$(document).ready(function(){
    $('input[type=radio]').click(function(){
        if(this.value=="yes"){ // this means they are importing history
          eel.import_history() // trigger the filedialog to open .ini file

          var columnField = document.getElementById("column");
          columnField.removeAttribute("enabled", "");
          columnField.setAttribute("disabled", "");
          var statField = document.getElementById("statistic");
          statField.removeAttribute("enabled", "");
          statField.setAttribute("disabled", "");
          var repsField = document.getElementById("repetitions");
          repsField.removeAttribute("enabled", "");
          repsField.setAttribute("disabled", "");
          //show these elements bc they do have the history, but leave them disabled in the html
          var completedField = document.getElementById("completedDiv");
          completedField.style.display = "block";
          var completedField = document.getElementById("outOf");
          completedField.style.display = "block";

        } else { // this means they're not importing history
          var columnField = document.getElementById("column");
          columnField.removeAttribute("disabled", "");
          columnField.setAttribute("enabled", "");
          var statField = document.getElementById("statistic");
          statField.removeAttribute("disabled", "");
          statField.setAttribute("enabled", "");
          var repsField = document.getElementById("repetitions");
          repsField.removeAttribute("disabled", "");
          repsField.setAttribute("enabled", "");
          // hide these elements because they have no history yet
          var completedField = document.getElementById("completedDiv");
          completedField.style.display = "none";
          var completedField = document.getElementById("outOf");
          completedField.style.display = "none";

        }
    });
});

function flipClicked() {
  clicked = true;
}

function getPathToFile() {
  console.log("just got to getPathToFile");
  eel.get_csv()(setScreen);
}

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

// this function will hide the settings section and show the progress section
function hideUnhide(form) {
  console.log("just got to hideUnhide");
  var col = form.column.value;
  var stat = form.statistic.value;
  var reps = form.repetitions.value;
  var com = form.completed.value;
  // if nothing is input into the completed reps field, make it 0
  if(com=="" || com== null){
    var com = 0;
  }
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

function pauseProgress(){
  console.log("YOU ARE IN PAUSEPROGRESS()")
  eel.write_config()
}

function updateProgressAndCallSample(perc) {
  console.log("inside updateProgressAndCallSample()")
  console.log(perc)
  var progress = document.getElementById("progress");
  progress.style.width = perc;
  progress.innerHTML = perc;
  /*document.getElementById('pause').onclick = function() {
     pauseProgress();
  }​;​*/
  if(clicked){
    pauseProgress();
  } else {
    eel.sample();
  }
}
eel.expose(updateProgressAndCallSample)

function endProgress(){
  alert_string = eel.calculate_bootstrapped_values()

}
eel.expose(endProgress)

function showBoostrapAlert(alert_string){
  alert(alert_string);
}
eel.expose(showBoostrapAlert)

function updateConfigs(col_name, com_reps, total_reps, stat){
  var select = document.getElementById("column");
  var col = col_name;
  var el = document.createElement("option");
  el.textContent = col;
  el.value = col;
  select.add(el);
  document.getElementById("completed").value = com_reps;
  document.getElementById("repetitions").value = total_reps;
  document.getElementById("statistic").value = stat;
}
eel.expose(updateConfigs)
