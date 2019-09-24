#!/usr/bin/node
// a script that imports an array and computes a new array.
const list = require('./100-data').list;

const new_list = list.map(x => list[x - 1] * (x - 1));
console.log(list);
console.log(new_list);
