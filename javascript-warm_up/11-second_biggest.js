#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const nums = process.argv.map(x => parseInt(x, 10));
  console.log(nums.sort(function (a, b) { return a - b; }).slice(-2)[0]);
}
