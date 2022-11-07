const fs = require("fs");
console.log("------------------------------------------------------------------------------------------------------------------")
// without promises
// reading other files inside callback functions of parent functions
var dummy = fs.readFile("./Stopping by Woods on a Snowy Evening.txt", function(error_1,  woods){
    fs.readFile("./Dust of Snow.txt", function(error_2, dust){
        fs.readFile("./Birches.txt", function(error_3, birches){
            console.log(woods.toString());
            console.log(dust.toString());
            console.log(birches.toString());
        });
    });
});
console.log("------------------------------------------------------------------------------------------------------------------")
// using promise all
// this takes an array of tasks and returns an array of newly generated promises
const utils = require("util");

// creates a promise instance of fs.readFile() method
const rFile = utils.promisify(fs.readFile);

Promise.all([   // an array of promises
    rFile("./Stopping by Woods on a Snowy Evening.txt"),
    rFile("./Dust of Snow.txt"),
    rFile("./Birches.txt")
])
.then(function(data){   // callback for resolved promise
    const [data_1, data_2, data_3] = data;  // similar to tuple unpacking, but in reverse
    console.log(data_1.toString());
    console.log(data_2.toString());
    console.log(data_3.toString());
},
function(error){    // callback for rejected promise
    console.log(error);
});
