function renderTeacherView(courses) {
    const courseTable = document.getElementById("course-table");
    const tbody = courseTable.querySelector("tbody");
    tbody.innerHTML = ""; // Clear existing content
    
    courses.forEach(course => {
        // Create table row for each course
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${course.student}</td>
            <td>${course.grade}</td>
        `;
        tbody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", function() {

    
    // function fetchTeacherView() {
    //     fetch("/get-teacher-view")
    //     .then(response => response.json())
    //     .then(data => {
    //         // Call the renderTeacherCourses function defined outside the scope
    //         renderTeacherView(data);

    //         // const courseName = data.courseName; // Assuming the course name is included in the response data
    //         // document.getElementById('your-courses').innerText = courseName;
    //     })
    //     .catch(error => console.error('Error fetching teacher courses:', error));
    // }


    function fetchTeacherView(classId) {
        fetch(`/get-teacher-view/${classId}`) // Fetch data for the specific class
        .then(response => response.json())
        .then(data => {
            renderTeacherView(data); // Render the teacher view data
        })
        .catch(error => console.error('Error fetching teacher view:', error));
    }

    // const urlParams = new URLSearchParams(window.location.search);
    // const classId = urlParams.get('class_id');
    // console.log('Class ID:', classId);

    const classId = window.location.pathname.split('/').pop();
    console.log('Class ID:', classId);

    fetchTeacherView(classId);
});