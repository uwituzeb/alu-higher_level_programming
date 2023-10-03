#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const result = {};
  
      for (const task of JSON.parse(body)) {
        if (task.completed === true) {
          if (task.userId in result) {
            result[task.userId]++;
          } else {
            result[task.userId] = 1;
          }
        }
      }
      console.log(result);
    }
  });