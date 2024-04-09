function renderTeacherView(courses) {
    const courseTable = document.getElementById("course-table");
    const tbody = courseTable.querySelector("tbody");
    tbody.innerHTML = "";
    
    courses.forEach(course => {
        // Creates table row for each course
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${course.student}</td>
            <td>${course.grade}</td>
        `;
        tbody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", function() {

    function fetchTeacherView(classId) {
        fetch(`/get-teacher-view/${classId}`)
        .then(response => response.json())
        .then(data => {
            renderTeacherView(data);
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