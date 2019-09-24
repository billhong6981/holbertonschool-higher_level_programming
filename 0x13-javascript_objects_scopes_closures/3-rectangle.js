#!/usr/bin/node
// defines Rectangle class with attributes

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  };
  print() {
    let s = "";
    for (let i = 0; i < this.height; i++) {
      if (i != this.height - 1) {
	s += "X".repeat(this.width) + "\n";
      } else {
	s += "X".repeat(this.width);
      }
    }
    console.log(s);
  };
}
module.exports = Rectangle;
