#!/usr/bin/node
const argVar = process.argv.length;
console.log(argVar === 2 ? 'No argument' : argVar === 3 ? 'Argument found' : 'Arguments found');
