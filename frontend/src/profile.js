window.addEventListener('DOMContentLoaded', async function() {
    try {
        // Fetch user role from the backend after signing in
        const response = await fetch('http://your-backend-api.com/user-role', {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer <your-access-token>'
            }
        });

        if (response.ok) {
            const userRole = await response.json();
            displayProfileContent(userRole);
        } else {
            console.error('Failed to fetch user role');
        }
    } catch (error) {
        console.error('Error fetching user role:', error.message);
    }
});

function displayProfileContent(userRole) {
    const profileContent = document.getElementById('profileContent');

    // Dynamically generate content based on user role
    if (userRole === 'nanny') {
        profileContent.innerHTML = '<h2>Welcome, Nanny!</h2><p>Your profile content for nannies goes here.</p>';
    } else if (userRole === 'family') {
        profileContent.innerHTML = '<h2>Welcome, Family!</h2><p>Your profile content for families looking for nannies goes here.</p>';
    } else {
        profileContent.innerHTML = '<h2>Welcome, User!</h2><p>Your profile content for general users goes here.</p>';
    }
}

