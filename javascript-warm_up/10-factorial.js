#!/usr/bin/node
function factorial (num) {
  const n = parseInt(num, 10);
  if (isNaN(n) || n < 2) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
console.log(factorial(process.argv[2]));
