// Function to handle user registration
async function signUp(username, email, password) {
    try {
        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        if (response.ok) {
            const userData = await response.json();
            console.log('User signed up successfully:', userData);
            return userData;
        } else {
            const errorMessage = await response.text();
            throw new Error(errorMessage);
        }
    } catch (error) {
        console.error('Error signing up:', error.message);
        throw error;
    }
}

// Function to list a nanny job by a provider
async function listNannyJob(nannyJobData) {
    try {
        const response = await fetch('/api/nanny-jobs/list', {
            method: 'POST',
            body: nannyJobData
        });

        if (!response.ok) {
            throw new Error('Failed to list nanny job. Please try again.');
        }

        const responseData = await response.json();
        console.log('Nanny job listed successfully:', responseData);
    } catch (error) {
        console.error('Error listing nanny job:', error.message);
    }
}

// Function to search nanny jobs with filters
async function searchNannyJobsWithFilters(filters) {
    try {
        const response = await fetch('/api/nanny-jobs/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(filters)
        });

        if (!response.ok) {
            throw new Error('Failed to search nanny jobs. Please try again.');
        }

        const nannyJobs = await response.json();
        displaySearchResults(nannyJobs);
        displayNannyJobsOnMap(nannyJobs);
    } catch (error) {
        console.error('Error searching nanny jobs:', error.message);
    }
}

// Function to save a nanny job as a favorite for a user
async function saveFavoriteNannyJob(userId, nannyJobId) {
    try {
        const response = await fetch(`/api/users/${userId}/favorites`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nannyJobId })
        });

        if (!response.ok) {
            throw new Error('Failed to save nanny job as favorite. Please try again.');
        }

        console.log('Nanny job saved as favorite successfully.');
    } catch (error) {
        console.error('Error saving nanny job as favorite:', error.message);
    }
}

// Event listener for user registration form submission
document.getElementById('signUpForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    await signUp(username, email, password);
});

// Event listener for nanny job listing form submission (for providers)
document.getElementById('listNannyJobForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const nannyJobData = new FormData(this);
    await listNannyJob(nannyJobData);
});

// Event listener for nanny job search form submission (for families)
document.getElementById('nannyJobSearchForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const searchFilters = {}; // Implement logic to collect search filters from the form
    await searchNannyJobsWithFilters(searchFilters);
});

// Event listener for saving a nanny job as favorite
document.getElementById('saveFavoriteBtn').addEventListener('click', async function(event) {
    event.preventDefault(); // Prevent default link behavior
    const userId = 'user123'; // Replace with the logged-in user's ID
    const nannyJobId = 'nannyJob456'; // Replace with the ID of the nanny job to save
    await saveFavoriteNannyJob(userId, nannyJobId);
});

