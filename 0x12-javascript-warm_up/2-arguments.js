#!/usr/bin/node
const len_arg = process.argv.length;
console.log(len_arg === 2 ? 'No argument' : len_arg === 3 ? 'Argument found' : 'Arguments found');
