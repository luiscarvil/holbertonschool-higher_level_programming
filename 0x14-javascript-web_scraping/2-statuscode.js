#!/usr/bin/node
const linkUrl = process.argv[2];
const request = require('request');
request(linkUrl, function (error, response) {
  if (error) return console.log(error);
  console.log('code: ' + response.statusCode);
});
