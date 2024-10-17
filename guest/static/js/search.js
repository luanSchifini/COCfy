console.log('iniciando')
// Ensure that the input and box elements exist
const input = document.getElementById('search_here');
const box = document.getElementById('box'); // Reference the suggestion box

input.addEventListener('keyup', (e) => {
    console.log(e)
    const searchTerm = e.target.value.toLowerCase();
    box.innerHTML = ""; // Clear the suggestions box

    if (searchTerm.length === 0) {
        return; // If the input is empty, don't display anything
    }

    // Filter the student names based on the search term
    const filteredArr = data.filter(info =>
        info['student_name'].toLowerCase().includes(searchTerm)
    );

    // Display the results
    if (filteredArr.length > 0) {
        filteredArr.forEach(info => {
            box.innerHTML += `<b>${info['student_name']}</b><br>`;
        });
    } else {
        box.innerHTML = "<b>No results found...</b>";
    }
});

