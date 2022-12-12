#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/';
url += process.argv[2];

request(url, function (error, response) {
  if (!error) {
    const body = JSON.parse(response.body);
    console.log(body.title);
  }
});
