//Function for ...
function funcOne(){
  const url = ""; //Fill In - Complete Later

  fetch(url)
    .then((res) => {
      return res.json();
    })
    .then((jsonResult) => {
      console.log("success");
    }) //If successful
    .catch((error) => {
      console.log("error");
    })     //If failure
}
