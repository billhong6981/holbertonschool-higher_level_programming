#!/usr/bin/node
// prints the number of movie that character “Wedge Antilles” is present

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const dict = JSON.parse(body);
  const results = dict.results;
  let count = 0;
  results.forEach(result => {
    const character = result.characters;
    for (let i = 0; i < character.length; i++) {
      if (character[i] === 'https://swapi.co/api/people/18/') {
        count++;
      }
    }
  });
  console.log(count);
});
