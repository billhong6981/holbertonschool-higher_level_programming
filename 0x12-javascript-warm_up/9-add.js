#!/usr/bin/node
//addition function
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add(a, b) {
  if (!a) {
    return (a);
  } else if (!b) {
    return (b);
  } else if (a && b) {
    return (a + b);
  }
}
console.log(add(a, b));
