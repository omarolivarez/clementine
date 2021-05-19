var clicked = false;
var p = document.getElementById("pause");

function flipClicked() {
  clicked = true;
}
/*p.addEventListener('click', flipClicked);​
function flipClicked() {
  clicked = true;
}
p.addEventListener("click", function() {
   clicked = true
}​);​*/
/*
document.addEventListener('DOMContentLoaded', init, false);
function init(){
  function flipClicked() {
    clicked = true;
  }


  console.log(progress.innerHTML)
  //p.addEventListener('click', flipClicked);​
};*/

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

function hideUnhide(form) {
  console.log("just got to hideUnhide");
  var col = form.column.value;
  var stat = form.statistic.value;
  var reps = form.repetitions.value;
  var com = form.completed.value;
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
  alert("Bootstrapping complete!");
}
eel.expose(endProgress)
