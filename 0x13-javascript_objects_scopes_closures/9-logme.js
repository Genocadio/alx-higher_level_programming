#!/usr/bin/node
let count;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
