#!/usr/bin/node
const arg = process.argv[2];
const fs = require('fs');
fs.readFile(arg, 'utf-8', function (err, data) {
  if (err) return console.log(err);
  console.log(data);
});
