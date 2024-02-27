document.getElementById('searchForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const minSalary = document.getElementById('minSalary').value;
    const maxSalary = document.getElementById('maxSalary').value;
    const requirements = document.getElementById('requirements').value;

    const queryParams = new URLSearchParams({
        location,
        minSalary,
        maxSalary,
        requirements
    });

    try {
        const response = await fetch(`/api/nanny-jobs/search?${queryParams}`);

        if (response.ok) {
            const data = await response.json();
            displaySearchResults(data);
        } else {
            console.error('Search failed');
            // Display error message to the user
        }
    } catch (error) {
        console.error('Error searching:', error.message);
    }
});

function displaySearchResults(results) {
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = '';

    if (results.length === 0) {
        searchResultsDiv.textContent = 'No results found';
        return;
    }

    results.forEach(result => {
        // Create a container for each nanny job
        const jobContainer = document.createElement('div');
        jobContainer.classList.add('job-container');

        // Create elements for nanny job details (e.g., job title, salary, etc.)
        const jobTitle = document.createElement('h2');
        jobTitle.textContent = result.title; // Assuming 'title' is a property of the search result object
        jobContainer.appendChild(jobTitle);

        const jobSalary = document.createElement('p');
        jobSalary.textContent = `Salary: ${result.salary}`; // Assuming 'salary' is a property of the search result object
        jobContainer.appendChild(jobSalary);

        const jobRequirements = document.createElement('p');
        jobRequirements.textContent = `Requirements: ${result.requirements}`; // Assuming 'requirements' is a property of the search result object
        jobContainer.appendChild(jobRequirements);

        // Append job container to search results div
        searchResultsDiv.appendChild(jobContainer);
    });
}

