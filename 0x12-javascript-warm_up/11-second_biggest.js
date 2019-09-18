#!/usr/bin/node
//prints second biggest number
const array = process.argv;
if (array.length < 4) {
  console.log('0');
}
let max_1 = array[2];
let max_2 = 0;
for (let i = 3; i < array.length; i++) {
  if (array[i] > max_1) {
    max_2 = max_1;
    max_1 = array[i];
  } else if (array[i] < max_1 && array[i] > max_2) {
    max_2 = array[i];
  }
}
console.log(max_2);
