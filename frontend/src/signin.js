document.getElementById('signInForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const userData = await response.json();
            // Redirect to profile page based on user type
            if (userData.type === 'nanny') { // Assuming 'nanny' is the user type for nanny jobs
                window.location.href = 'nanny_profile.html'; // Redirect to the nanny profile page
            } else {
                console.error('Invalid user type');
                // Handle invalid user type error
            }
        } else {
            console.error('Sign-in failed');
            // Display error message to the user
        }
    } catch (error) {
        console.error('Error signing in:', error.message);
    }
});

