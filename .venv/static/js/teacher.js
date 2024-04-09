function renderTeacherCourses(courses) {
    const courseTable = document.getElementById("course-table");
    const tbody = courseTable.querySelector("tbody");
    tbody.innerHTML = ""; // Clear existing content
    
    courses.forEach(course => {
        // Create table row for each course
        const row = document.createElement("tr");
        row.innerHTML = `
            <td><a href="/class/${course.class_id}">${course.courseName}</a></td>
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