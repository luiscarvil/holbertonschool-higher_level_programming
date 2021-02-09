#!/usr/bin/node
const idMovie = process.argv[2];
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + idMovie, function (error, response, body) {
  if (error) return console.log(error);
  console.log(JSON.parse(body).title);
});
