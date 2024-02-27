document.getElementById('signupForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        if (response.ok) {
            // Assuming the server responds with user data upon successful sign-up
            const userData = await response.json();
            // Redirect to profile page based on user type
            if (userData.type === 'buyer') {
                window.location.href = 'buyer_profile.html';
            } else if (userData.type === 'seller') {
                window.location.href = 'seller_profile.html';
            } else if (userData.type === 'renter') {
                window.location.href = 'renter_profile.html';
            } else {
                console.error('Invalid user type');
                // Handle invalid user type error
            }
        } else {
            console.error('Sign-up failed');
            // Display error message to the user
        }
    } catch (error) {
        console.error('Error signing up:', error.message);
    }
});

