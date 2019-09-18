#!/usr/bin/node
//prints square
const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Missing size');
} else {
  let x = '';
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      x += 'X';
    }
    if (i !== arg - 1) {
      x += '\n';
    }
  }
  console.log(x);
}
