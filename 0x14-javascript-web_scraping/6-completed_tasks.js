#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
const dictCount = {};
request(arg, function (error, response, body) {
  if (error) return console.log(error);
  const dictJson = (JSON.parse(body));
  for (let i = 0; i < dictJson.length; i++) {
    if (dictJson[i].completed === true) {
      if (dictCount[dictJson[i].userId] === undefined) {
        dictCount[dictJson[i].userId] = 1;
      } else {
        dictCount[dictJson[i].userId]++;
      }
    }
  }
  console.log(dictCount);
});
