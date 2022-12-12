#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const toFile = process.argv[3];

request(url, function (error, response) {
  if (!error) {
    const body = response.body;
    fs.writeFile(toFile, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
