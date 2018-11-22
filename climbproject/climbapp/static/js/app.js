$(document).foundation()

//foundation nav bar
$("[data-menu-underline-from-center] a").addClass("underline-from-center");

// function myFunction(name,job) {
//     document.getElementById("demo").innerHTML =
//     "Welcome " + name + ", the " + job + ".";
// }

function inOrOut(boolValCheck) {
  if(boolValCheck == true){
    document.getElementById("demo").innerHTML =
    "Indoor"
    // document.getElementById("demo").innerHTML =
    // "Welcome " + name + ", the " + job + ".";
  }else{
    document.getElementById("demo").innerHTML =
    "Outdoor"
  }
}

// Comment feedback
function checkComment() {
  if(boolValCheck == true){
    document.getElementById("demo").innerHTML =
    "Indoor"
    // document.getElementById("demo").innerHTML =
    // "Welcome " + name + ", the " + job + ".";
  }else{
    document.getElementById("demo").innerHTML =
    "Outdoor"
  }
}
