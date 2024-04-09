function renderYourCourses() {

    var yourCoursesButton = document.getElementById('your-courses');
    var addCoursesButton = document.getElementById('add-courses');

    yourCoursesButton.style.backgroundColor = '#4472c4';
    yourCoursesButton.style.color = '#fff';
    addCoursesButton.style.backgroundColor = '#b4c7e7';
    addCoursesButton.style.color = 'black';

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var courses = JSON.parse(xhttp.responseText);
            renderCoursesTable(courses, true);
        }
    };
    xhttp.open("GET", "/student/your-courses");
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
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var courses = JSON.parse(xhttp.responseText);
            renderCoursesTable(courses, false);
        }
    };
    xhttp.open("GET", "/student/add-courses");
    xhttp.send();
}

function renderCoursesTable(courses, isYourCourses) {
    var table = document.getElementById("courses-table");
    table.innerHTML = ""; // Clear previous content

    var headerRow = table.insertRow(0);
    var headers = ["Course Name", "Teacher", "Time", "Students Enrolled"];
    if (!isYourCourses) {
        headers.push("Add class");
    }
    headers.forEach(function(header) {
        var cell = headerRow.insertCell();
        cell.innerHTML = header;
    });

    var enrolledCourses = new Set(); // Set to store enrolled courses

    // Fetch the list of enrolled courses
    if (isYourCourses) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                var enrolled = JSON.parse(xhttp.responseText);
                enrolled.forEach(function(course) {
                    enrolledCourses.add(course.courseName);
                });
                addRows();
            }
        };
        xhttp.open("GET", "/student/your-courses");
        xhttp.send();
    } else {
        addRows();
    }

    function addRows() {
        courses.forEach(function(course) {
            var row = table.insertRow();
            var cell1 = row.insertCell();
            cell1.innerHTML = course.courseName;
            var cell2 = row.insertCell();
            cell2.innerHTML = course.teacher;
            var cell3 = row.insertCell();
            cell3.innerHTML = course.time;
            var cell4 = row.insertCell();
            cell4.innerHTML = course.enrollment;
            if (!isYourCourses) {
                var cell5 = row.insertCell();
                if (enrolledCourses.has(course.courseName)) {
                    cell5.innerHTML = "<button class='unenroll' onclick=\"unenroll('" + course.courseName + "')\">-</button>";
                } else {
                    cell5.innerHTML = "<button class='enroll' onclick=\"enroll('" + course.courseName + "')\">+</button>";
                }
            }
        });
    }
}


// function renderCoursesTable(courses, isYourCourses) {
//     var table = document.getElementById("courses-table");
//     table.innerHTML = ""; // Clear previous content

//     var headerRow = table.insertRow(0);
//     var headers = ["Course Name", "Teacher", "Time", "Students Enrolled"];
//     if (!isYourCourses) {
//         headers.push("Add class");
//     }
//     headers.forEach(function(header) {
//         var cell = headerRow.insertCell();
//         cell.innerHTML = header;
//     });

//     courses.forEach(function(course) {
//         var row = table.insertRow();
//         var cell1 = row.insertCell();
//         cell1.innerHTML = course.courseName;
//         var cell2 = row.insertCell();
//         cell2.innerHTML = course.teacher;
//         var cell3 = row.insertCell();
//         cell3.innerHTML = course.time;
//         var cell4 = row.insertCell();
//         cell4.innerHTML = course.enrollment;
//         if (!isYourCourses) {
//             var cell5 = row.insertCell();
//             cell5.innerHTML = "<button class='enroll' onclick=\"enroll('" + course.courseName + "')\">+</button>";
//         }
//     });
// }

function enroll(courseName) {
    // Handle enrollment logic here
}

function unenroll(courseName) {
    // Handle unenrollment logic here
}