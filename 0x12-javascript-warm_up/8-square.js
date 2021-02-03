#!/usr/bin/node
const vSize = process.argv[2];
if (isNaN(parseInt(vSize))) console.log('Missing size');
for (let i = 0; i < vSize; i++) console.log('X'.repeat(vSize));
