function slide() {
  var x = document.getElementsByClassName("slide");
  for (var i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(slide, 5000); // set time
}