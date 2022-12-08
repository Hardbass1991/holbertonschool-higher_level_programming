#!/usr/bin/node
const Squar = require('./5-square');

module.exports = class Square extends Squar {
  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let i = 0; i < this.width; i++) {
          line = line.concat(c);
        }
        console.log(line);
      }
    }
  }
};
