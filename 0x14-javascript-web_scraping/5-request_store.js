#!/usr/bin/node
const arg = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');
request(arg, 'utf-8', function (error, response, body) {
  if (error) return console.log(error);
  fs.writeFile(file, body, function (err) {
    if (err) return console.log(err);
  });
});
