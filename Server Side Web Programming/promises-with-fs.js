// importing the filesystem module
const filesystem = require("fs");

console.log("Reading in a text file without promises!");
console.log("-----------------------------beginning-file-read-operation----------------------------------------------");

var poem = filesystem.readFile("./Stopping by Woods on a Snowy Evening.txt", function(error, file){     // an async callback
    console.log(file.toString());   // no error handling here
});                            // the callback function for error is left dangling!
console.log("This was executed asynchronously!");
console.log("--------------------------------------------------------------------------------------------------------");


// doing the same with promises!
console.log("Reading in a text file with promises!");
console.log("--------------------------------------------------------------------------------------------------------");


new Promise(function(resolved, rejected){
filesystem.readFile("./Stopping by Woods on a Snowy Evening.txt", function(error, data){ // callback
    if (error){
        rejected("File read operation has failed!");
    } else if (data != null){
        resolved(data.toString());
    }
  });
})
.then(function(value){        // callback for resolved promise
    console.log(value);    // print the string
},
function(error){        // callback for rejected promise
    console.log(error);
})

console.log("--------------------------------------------------------------------------------------------------------");
