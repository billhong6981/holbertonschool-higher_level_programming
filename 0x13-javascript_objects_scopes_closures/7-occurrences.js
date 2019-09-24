#!/usr/bin/node
// prints numbers of occurence for the search element in a array

exports.nbOccurences = function (list, searchElement) {
  if (!list || !searchElement) {
    return undefined;
  }
  let nb = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] == searchElement) {
      nb++;
    }
  }
  return nb;
}
