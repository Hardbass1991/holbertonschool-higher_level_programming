#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      sum += 1;
    }
  });
  return sum;
};
