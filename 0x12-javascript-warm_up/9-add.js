#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Please provide two valid integers as arguments.');
} else {
  const result = add(arg1, arg2);
  console.log(`The addition of ${arg1} and ${arg2} is: ${result}`);
}
