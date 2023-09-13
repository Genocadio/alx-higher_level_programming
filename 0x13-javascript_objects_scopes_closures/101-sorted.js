#!/usr/bin/node

const data = require('./101-data').dict;

const newObj = {};

for (const key in data) {
  const value = data[key];
  if (newObj[value]) {
    newObj[value].push(key);
  } else {
    newObj[value] = [key];
  }
}

console.log(newObj);
