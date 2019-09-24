#!/usr/bin/node
// a function that prints numbers of argument and value

let count = 0;
exports.logMe = function (item) {
  let np = "";
  np = count + ": " + item;
  count++;
  console.log(np);
};
