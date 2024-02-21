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

// Function to list a property by a seller
async function listProperty(propertyData) {
    try {
        const response = await fetch('/api/properties/list', {
            method: 'POST',
            body: propertyData
        });

        if (!response.ok) {
            throw new Error('Failed to list property. Please try again.');
        }

        const responseData = await response.json();
        console.log('Property listed successfully:', responseData);
    } catch (error) {
        console.error('Error listing property:', error.message);
    }
}

// Function to search properties with filters
async function searchPropertiesWithFilters(filters) {
    try {
        const response = await fetch('/api/properties/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(filters)
        });

        if (!response.ok) {
            throw new Error('Failed to search properties. Please try again.');
        }

        const properties = await response.json();
        displaySearchResults(properties);
        displayPropertiesOnMap(properties);
    } catch (error) {
        console.error('Error searching properties:', error.message);
    }
}

// Function to save a property as a favorite for a user
async function saveFavoriteProperty(userId, propertyId) {
    try {
        const response = await fetch(`/api/users/${userId}/favorites`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ propertyId })
        });

        if (!response.ok) {
            throw new Error('Failed to save property as favorite. Please try again.');
        }

        console.log('Property saved as favorite successfully.');
    } catch (error) {
        console.error('Error saving property as favorite:', error.message);
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

// Event listener for property listing form submission (for sellers)
document.getElementById('listPropertyForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const propertyData = new FormData(this);
    await listProperty(propertyData);
});

// Event listener for property search form submission (for buyers)
document.getElementById('propertySearchForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const searchFilters = {}; // Implement logic to collect search filters from the form
    await searchPropertiesWithFilters(searchFilters);
});

// Event listener for saving a property as favorite
document.getElementById('saveFavoriteBtn').addEventListener('click', async function(event) {
    event.preventDefault(); // Prevent default link behavior
    const userId = 'user123'; // Replace with the logged-in user's ID
    const propertyId = 'property456'; // Replace with the ID of the property to save
    await saveFavoriteProperty(userId, propertyId);
});

