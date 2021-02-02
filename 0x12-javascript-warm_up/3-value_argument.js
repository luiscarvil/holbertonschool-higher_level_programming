#!/usr/bin/node
const arg_var = process.argv;
console.log(arg_var[2] === undefined ? 'No argument': arg_var[2]);
