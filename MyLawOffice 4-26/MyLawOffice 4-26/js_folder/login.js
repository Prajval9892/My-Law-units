var url_init = "http://127.0.0.1:8000/";

function login() {
    // var email = document.getElementById("emailaddress").value;
    // var password = document.getElementById("password").value;

    // Fetch CSRF token from a hidden input field in your HTML
    // var csrfToken = document.getElementById("csrf_token").value;

    var request_data = {
        method: "GET",
        
    };

    fetch(url_init + "login", request_data)
        .then(response => {
            // Handle response
        })
        .catch(error => {
            // Handle error
        });
}
