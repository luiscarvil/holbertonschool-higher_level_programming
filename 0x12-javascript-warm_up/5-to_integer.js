#!/usr/bin/node
const argVar = parseInt(process.argv[2]);
console.log(isNaN(argVar) ? 'Not a number' : 'My number: '+ argVar);
