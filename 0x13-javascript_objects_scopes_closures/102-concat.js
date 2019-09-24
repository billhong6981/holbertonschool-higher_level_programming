#!/usr/bin/node
// a script that concats 2 files.

const order = `cat ${process.argv[2]} ${process.argv[3]} > ${process.argv[4]}`;

require('child_process').execSync(order).toString('UTF-8');
