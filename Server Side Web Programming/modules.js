// core node modules i.e built in modules
const http = require("http");
const https = require("https");

const server = http.createServer(function (request, response) {
    // dummy code
})

// to take inputs from console
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });


// local modules - user designed modules
// since this module is in the same directory path is "./"
const factorial = require("./local_module.js");

// check the import
readline.question("Enter an integer!", function(value){
    const result = factorial(value);
    console.log("Factorial of %n% is ".replace("%n%", value), result);
    readline.close();
});


