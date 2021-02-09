#!/usr/bin/node
const file = process.argv[2];
const stringW = process.argv[3];
const fs = require('fs');
fs.writeFile(file, stringW, function (err) {
  if (err) return console.log(err);
});
