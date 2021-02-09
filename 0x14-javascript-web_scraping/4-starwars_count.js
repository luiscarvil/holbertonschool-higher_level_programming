#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
let count = 0;
request(arg, function (error, response, body) {
  if (error) return console.log(error);
  const dictJson = (JSON.parse(body).results);
  for (let i = 0; i < dictJson.length; i++) {
    for (let j = 0; j < dictJson[i].characters.length; j++) {
      if (dictJson[i].characters[j].includes('/18/')) count++;
    }
  }
  console.log(count);
});
