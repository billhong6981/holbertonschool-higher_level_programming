#!/usr/bin/node
// a function that returns reversed a list

exports.esrever = function (list) {
  if (!list) {
    return undefined;
  }
  const len = list.length - 1;
  for (let i = 0; i <= Math.floor(len / 2); i++) {
    let temp = list[i];
    list[i] = list[len - i];
    list[len - i] = temp;
  }
  return list;
};
