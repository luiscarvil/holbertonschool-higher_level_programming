#!/usr/bin/node
const argVar = process.argv;
console.log(argVar[2] === undefined ? 'No argument' : argVar[2]);
