#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (!error) {
    const body = JSON.parse(response.body);
    const searchedChar = 'https://swapi-api.hbtn.io/api/people/18/';
    let n = 0;
    for (let i = 0; i < body.results.length; i++) {
      if (body.results[i].characters.includes(searchedChar)) {
        n += 1;
      }
    }
    console.log(n);
  }
});
