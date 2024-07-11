#!/usr/bin/node

const request = require('request');
// Import the 'request' module to make HTTP requests.

const API_URL = 'https://swapi-api.hbtn.io/api';
// Define the base URL for the Star Wars API.

if (process.argv.length > 2) {
  // Check if there are more than 2 arguments passed to the script.
  // process.argv contains command line arguments; the first two are 'node' and the script name.

  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // Make a GET request to fetch details of the film with ID provided as a command line argument.
    // The callback function has three parameters: error (err), response (_), and body (response body).

    if (err) {
      console.log(err);
      return;
      // If there's an error with the request, log it and exit the function.
    }

    const charactersURL = JSON.parse(body).characters;
    // Parse the JSON response body to get the array of character URLs.

    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          // For each character URL, create a new Promise.
          // Make a GET request to fetch the character details.
          // The callback function has three parameters: promiseErr (error), response (__), and charactersReqBody (response body).

          if (promiseErr) {
            reject(promiseErr);
            // If there's an error with the request, reject the Promise.
            return;
          }

          resolve(JSON.parse(charactersReqBody).name);
          // Parse the JSON response body to get the character's name.
          // Resolve the Promise with the character's name.
        });
      })
    );

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      // Wait for all Promises to resolve and join the character names with a newline.
      // Print the names to the console.

      .catch(allErr => console.log(allErr));
    // If any of the Promises are rejected, catch the error and log it.
  });
}
