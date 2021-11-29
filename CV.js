function Name() {
    console.log("shahar");
}

function validateINFO() {
    let obj = document.getElementById("Email");
    let emailOK = obj.checkValidity();
    if (emailOK) {
        alert("email is OK");
    }
    else {
        alert("check your email");
    }
}
