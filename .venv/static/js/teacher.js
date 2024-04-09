function renderYourCourses() {
    var yourCoursesButton = document.getElementById('your-courses');

    yourCoursesButton.style.backgroundColor = '#4472c4';
    yourCoursesButton.style.color = '#fff';
    

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/your-courses");
    xhttp.send();
}



