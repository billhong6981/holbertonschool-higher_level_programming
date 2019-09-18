#!/usr/bin/node
//function that executes x times a function
function callMeMoby (x, func) {
  for (let i = 0; i < x; i++) {
    func ();
  }
}
module.exports = {
  callMeMoby: callMeMoby
}
