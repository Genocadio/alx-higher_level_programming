#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative numbers is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 and 1 is 1
  }
  return n * factorial(n - 1); // Recursive case
}
const arg = parseInt(process.argv[2]);
const result = factorial(arg);
console.log(`The factorial of ${arg} is: ${result}`);
