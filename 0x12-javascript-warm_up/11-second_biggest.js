#!/usr/bin/node
function secondBiggestInteger () {
  const args = Array.from(arguments).map(Number);
  const uniqueArgs = [...new Set(args)];
  const sortedArgs = uniqueArgs.sort((a, b) => b - a);
  return sortedArgs[1] || 0;
}
console.log(secondBiggestInteger(1, 2, 3, 4, 5)); // 4
console.log(secondBiggestInteger(1, 2)); // 1
console.log(secondBiggestInteger()); // 0
