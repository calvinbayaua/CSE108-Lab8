document.getElementById('login-button').addEventListener('click', function() {
    var user = document.getElementById('username').value;
    var pass = document.getElementById('password').value;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({ username: user, password: pass }));
    xhttp.onload = function() {
        if (xhttp.status === 200) {
            console.log('Login successful');
            // Redirect to appropriate page after successful login
            window.location.href = xhttp.responseURL;
        } else if (xhttp.status === 401) {
            console.error('Invalid username or password');
            document.getElementById('username').value = "";
            document.getElementById('password').value = "";
        } else {
            console.error('Error occurred');
        }
    };
});

// function login() {
//     var user = document.getElementById('username').value;
//     var pass = document.getElementById('password').value;

//     var xhttp = new XMLHttpRequest();
//     xhttp.open("POST", "/", true); // Updated URL to point to the login route
//     xhttp.setRequestHeader('Content-Type', 'application/json');
//     xhttp.send(JSON.stringify({ username: user, password: pass }));
//     xhttp.onload = function() {
//         if (xhttp.status === 200) {
//             console.log('Login successful');
//             // Redirect to appropriate page after successful login
//             window.location.href = xhttp.responseURL;
//         } else if (xhttp.status === 401 || xhttp.status === 404) {
//             console.error('Retry login');
//             document.getElementById('username').value = "";
//             document.getElementById('password').value = "";
//         }
//     };
// }

// function login() {
//     var user = document.getElementById('username').value;
//     var pass = document.getElementById('password').value;

//     var xhttp = new XMLHttpRequest();
//     xhttp.open("POST", "/login", true);
//     xhttp.setRequestHeader('Content-Type', 'application/json');
//     xhttp.send(JSON.stringify({ username: user, password: pass }));
//     xhttp.onload = function() {
//         if (xhttp.status === 200) {
//             console.log('Login successful');
//         } else if (xhttp.status === 401 || xhttp.status === 404) {
//             console.error('Retry login');
//             document.getElementById('username').value = "";
//             document.getElementById('password').value = "";
//         }
//     };
// }