#!/usr/bin/node
const strPrint = "C is fun";
if (isNaN(parseInt(process.argv[2]))) console.log("Missing number of occurrences")
for(let i = 0; i < process.argv[2]; i++) console.log(strPrint);