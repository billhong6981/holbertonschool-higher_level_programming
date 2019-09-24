#!/usr/bin/node
// computes user_id occurrences

const dict = require('./101-data').dict;

let new_dict = {};
const entries = Object.entries(dict);
entries.forEach(entry => {
  if (entry[1] in new_dict) {
    new_dict[entry[1]].push(entry[0]);
  } else {
    new_dict[entry[1]] = [entry[0]];
  }
})
console.log(new_dict);
