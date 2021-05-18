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
  console.log(stat);
  console.log(reps);
  //var myElement = document.getElementById("column");
  //myElement.style.display = "none";
  /*document.getElementById("input").style.display = "none";
  document.getElementById("importHistory").style.display = "none";
  document.getElementById("gridRadios1").style.display = "none";
  document.getElementById("gridRadios2").style.display = "none";
  document.getElementById("column").style.display = "none";
  document.getElementById("statistic").style.display = "none";
  document.getElementById("repititions").style.display = "none";
  document.getElementById("begin").style.display = "none";

  document.getElementById("progress").style.display = "none";*/

}

function testResults (form) {
            var TestVar = form.inputbox.value;
            alert ("You typed: " + TestVar);
        }

$('form#begin').submit(function(e){
    //$(this).children('input[type=submit]').attr('disabled', 'disabled');
    // this is just for demonstration
    $("select#statistic").prop('disabled', true);
});
