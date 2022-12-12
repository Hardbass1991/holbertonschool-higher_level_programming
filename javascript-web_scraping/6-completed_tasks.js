#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, function (error, response) {
  if (!error) {
    const body = JSON.parse(response.body);
    for (let i = 0; i < body.length; i++) {
      const key = body[i].userId.toString();
      if (body[i].completed === true) {
        if (!Object.keys(dict).includes(key)) {
          dict[key] = 0;
        } else {
          dict[key] += 1;
        }
      }
    }
    console.log(dict);
  }
});
