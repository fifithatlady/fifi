const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API route to interact with the backend
app.post('/api/action', async (req, res) => {
    try {
        // Make a request to the backend (console.py) using axios
        const response = await axios.post('http://localhost:5000/api/action', req.body);

        // Forward the response from the backend to the frontend
        res.json(response.data);
    } catch (error) {
        // Handle errors
        console.error('Error:', error);
        res.status(500).json({ error: 'An error occurred' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

