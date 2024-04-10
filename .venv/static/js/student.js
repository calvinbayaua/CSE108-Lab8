function renderYourCourses() {
    var yourCoursesButton = document.getElementById('your-courses');
    var addCoursesButton = document.getElementById('add-courses');

    yourCoursesButton.style.backgroundColor = '#4472c4';
    yourCoursesButton.style.color = '#fff';
    addCoursesButton.style.backgroundColor = '#b4c7e7';
    addCoursesButton.style.color = 'black';

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/student/your-courses");
    xhttp.send();
    xhttp.onload = function() {
        var courses = JSON.parse(xhttp.responseText);
        var table = document.getElementById('courses-table');
        table.innerHTML = '<tr><th>Course Name</th><th>Teacher</th><th>Time</th><th>Students Enrolled</th>'

        courses.forEach(function(course) {
            var row = "<tr><td>" + course.name + "</td><td>" + course.teacher + "</td><td>" + course.time + "</td><td>" + course.enrollment + "</td></tr>";
            table.innerHTML += row;
        });
    }
}

function renderAddCourses() {
    var yourCoursesButton = document.getElementById('your-courses');
    var addCoursesButton = document.getElementById('add-courses');

    yourCoursesButton.style.backgroundColor = '#b4c7e7';
    yourCoursesButton.style.color = 'black';
    addCoursesButton.style.backgroundColor = '#4472c4';
    addCoursesButton.style.color = '#fff';

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/student/add-courses");
    xhttp.send();
    xhttp.onload = function() {
        var response = JSON.parse(xhttp.responseText);
        var enrolledCourses = response.enrolled_courses;
        var courses = response.courses;
        var table = document.getElementById('courses-table');
        table.innerHTML = '<tr><th>Course Name</th><th>Teacher</th><th>Time</th><th>Students Enrolled</th><th>Add Class</th>'

        courses.forEach(function(course) {
            var isEnrolled = enrolledCourses.some(function(enrolledCourse) {
                return enrolledCourse.name === course.name;
            });
            var buttonClass = isEnrolled ? 'unenroll' : 'enroll';
            var buttonText = isEnrolled ? '-' : '+';
            var row = "<tr><td>" + course.name + "</td><td>" + course.teacher + "</td><td>" + course.time + "</td><td>" + course.enrollment + "</td><td><button class='" + buttonClass + "' onclick='" + (isEnrolled ? "unenroll" : "enroll") + "(" + course.id + ")'>" + buttonText + "</button></td></tr>";
            table.innerHTML += row;
        });
    }
}

function enroll(courseId) {
    var xhttp = new XMLHttpRequest();
    var url = '/student/add-courses/enroll';
    xhttp.open("PUT", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ courseId: courseId }));
}

function unenroll(courseId) {
    var xhttp = new XMLHttpRequest();
    var url = '/student/add-courses/unenroll';
    xhttp.open("DELETE", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ courseId: courseId }));
}