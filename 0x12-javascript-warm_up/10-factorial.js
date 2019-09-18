#!/usr/bin/node
//prints factorial
const n = parseInt(process.argv[2]);
function factorial (n) {
  if (!n || n === 0 || n === 1) {
    return (1);
  }
  return (factorial(n - 1) * n);
}
console.log(factorial(n));
