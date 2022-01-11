
function getUsers() {
    let number = document.getElementById("id_number");
    fetch('https://reqres.in/api/users/'+number.value).then(
        response => response.json()
    ).then(
        (response_obj) => {
           return put_users_inside_html(response_obj.data)
        }
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj) {
    const curr_main = document.querySelector("main");

        const section = document.createElement('section');
        curr_main.innerHTML = `
        <img src="${response_obj.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj.name} </span>
            <br>
            <a href="mailto:${response_obj.email}">Send Email</a>
        </div>
        `;


}