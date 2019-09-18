#!/usr/bin/node
//a function that increments and calls a function
function addMeMaybe (x, func) {
  x++;
  func (x);
}
module.exports = {
  addMeMaybe: addMeMaybe
};
