#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const values = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(values, function(error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printAllCharacters(characters, 0);
  }
});

function printAllCharacters(characters, index) {
  request(characters[index], function(error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printAllCharacters(characters, index + 1);
      }
    }
  });
};
