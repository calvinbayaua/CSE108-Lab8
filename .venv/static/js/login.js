function login() {
    var user = document.getElementById('username').value;
    var pass = document.getElementById('password').value;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/login", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({ username: user, password: pass }));
    xhttp.onload = function() {
        if (xhttp.status === 200) {
            console.log('Login successful');
        } else if (xhttp.status === 401 || xhttp.status === 404) {
            console.error('Retry login');
            document.getElementById('username').value = "";
            document.getElementById('password').value = "";
        }
    };
}