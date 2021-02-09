#!/usr/bin/node
let indexCount = 0;
exports.logMe = function (item) {
  console.log(`${indexCount}: ${item}`);
  indexCount++;
};
