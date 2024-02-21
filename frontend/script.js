// Function to handle nanny search form submission
const nannySearchForm = document.querySelector('#nannySearchForm');
nannySearchForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(nannySearchForm);

    try {
        // Send POST request to backend API endpoint for nanny search
        const response = await fetch('https://fifthatlady.github.io/api/nannies/search', {
            method: 'POST',
            body: formData
        });

        // Check if request was successful
        if (response.ok) {
            // Parse response JSON
            const nannies = await response.json();

            // Display search results on the page (e.g., populate a list with nanny details)
            displaySearchResults(nannies);
        } else {
            // Display error message if nanny search failed
            const errorMessage = await response.text();
            alert(errorMessage);
        }
    } catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('Error:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
});

// Function to display search results on the page
function displaySearchResults(nannies) {
    // Implement logic to display search results (e.g., populate a list with nanny details)
    console.log(nannies);
}

