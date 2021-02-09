#!/usr/bin/node
// Square class that inherits from the Rectangle class

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
