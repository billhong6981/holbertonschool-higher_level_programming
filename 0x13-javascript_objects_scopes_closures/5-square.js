#!/usr/bin/node
// child class Square inherited from Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.width = size;
    this.height = size;
  };
}
module.exports = Square;
