#!/usr/bin/node
function numbFactorial(n){
    if (n === 0 || isNaN(n)) return 1;
    return (n * numbFactorial(n - 1));
}
console.log(numbFactorial(parseInt(process.argv[2])));