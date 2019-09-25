#!/usr/bin/node
// prints the number of movie that character “Wedge Antilles” is present

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const myRe = /https:\/\/swapi.co\/api\/people\/18\//g;
  console.log(body.match(myRe).length);
});
