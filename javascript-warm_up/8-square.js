#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    let line = '';
    for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
      line = line.concat('X');
    }
    console.log(line);
  }
}
