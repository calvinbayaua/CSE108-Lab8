function renderYourCourses() {
    var yourCoursesButton = document.getElementById('your-courses');
    var addCoursesButton = document.getElementById('add-courses');

    yourCoursesButton.style.backgroundColor = '#4472c4';
    yourCoursesButton.style.color = '#fff';
    addCoursesButton.style.backgroundColor = '#b4c7e7';
    addCoursesButton.style.color = 'black';

    var xhttp = new XMLHttpRequest();
    var url = '/student/your-courses';
    xhttp.open("GET", url);
    xhttp.send();
}

function renderAddCourses() {
    var yourCoursesButton = document.getElementById('your-courses');
    var addCoursesButton = document.getElementById('add-courses');

    yourCoursesButton.style.backgroundColor = '#b4c7e7';
    yourCoursesButton.style.color = 'black';
    addCoursesButton.style.backgroundColor = '#4472c4';
    addCoursesButton.style.color = '#fff';

    var xhttp = new XMLHttpRequest();
    var url = '/student/add-courses';
    xhttp.open("GET", url);
    xhttp.send();
}

function enroll(courseName) {
    var xhttp = new XMLHttpRequest();
    var url = '/student/add-courses/enroll';
    xhttp.open("PUT", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ courseName: courseName }));
}

function unenroll(courseName) {
    var xhttp = new XMLHttpRequest();
    var url = '/student/add-courses/unenroll';
    xhttp.open("DELETE", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ courseName: courseName }));
}