#!/usr/bin/node
// child class Square inherited from Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.width = size;
    this.height = size;
  };

  charPrint(c) {
    if (!c) {
      this.print();
    } else {
      let s = "";
      for (let i = 0; i < this.height; i++) {
	if (i != this.height - 1) {
	  s += c.repeat(this.width) + "\n";
	} else {
	  s += c.repeat(this.width);
	}
      }
      console.log(s);
    }
  };
}
module.exports = Square;
