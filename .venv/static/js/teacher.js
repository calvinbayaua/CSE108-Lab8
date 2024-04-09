// Define renderTeacherCourses function outside the scope of DOMContentLoaded event listener
// function renderTeacherCourses(courses) {
//     const courseTable = document.getElementById("course-table");
//     courseTable.innerHTML = ""; // Clear existing content
    
//     courses.forEach(course => {
//         // Create table row for each course
//         const row = document.createElement("tr");
//         row.innerHTML = `
//             <td>${course.courseName}</td>
//             <td>${course.teacher}</td>
//             <td>${course.time}</td>
//             <td>${course.enrollment}</td>
//         `;
//         courseTable.appendChild(row);
//     });
// }

function renderTeacherCourses(courses) {
    const courseTable = document.getElementById("course-table");
    const tbody = courseTable.querySelector("tbody");
    tbody.innerHTML = ""; // Clear existing content
    
    courses.forEach(course => {
        // Create table row for each course
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${course.courseName}</td>
            <td>${course.teacher}</td>
            <td>${course.time}</td>
            <td>${course.enrollment}</td>
        `;
        tbody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    // Function to fetch and render teacher courses
    function fetchTeacherCourses() {
        fetch("/get-teacher-courses")
        .then(response => response.json())
        .then(data => {
            // Call the renderTeacherCourses function defined outside the scope
            renderTeacherCourses(data);
        })
        .catch(error => console.error('Error fetching teacher courses:', error));
    }
    
    // Fetch and render teacher courses when the page loads
    fetchTeacherCourses();
});


// document.addEventListener("DOMContentLoaded", function() {

// function renderYourCourses(){
//     var yourCoursesButton = document.getElementById('your-courses');

//     yourCoursesButton.style.backgroundColor = '#4472c4';
//     yourCoursesButton.style.color = '#fff';
    

//     var xhttp = new XMLHttpRequest();
//     xhttp.open("GET", "/your-courses");
//     xhttp.send();
// }

// function fetchTeacherCourses(){
//     fetch("/get-teacher-courses")
//     .then(response => response.json())
//     .then(data => {
//         // Render the fetched data on the HTML page
//         renderTeacherCourses(data);
//     })
//     .catch(error => console.error('Error fetching teacher courses:', error));
// }


// // Fetch and render teacher courses when the page loads
//     fetchTeacherCourses();
//     renderYourCourses();

// });

