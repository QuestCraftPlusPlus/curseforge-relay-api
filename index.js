// Import modules
const express = require('express');
require('dotenv').config();

//Create expess app
const app = express();

// Start the API
app.listen(3000, () => {
    console.log('Api is accessible on port 3000');
})

// Call the curseforge API
const headers = {
    'Accept': 'application/json',
    'x-api-key': process.env.API_KEY
}

//Piggyback API listners
app.get('/getgameinfo', (req, res, next) => {
    
})