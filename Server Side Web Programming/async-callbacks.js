// import the filesystem module for read & write operations on external files
const FILESYS = require("fs");

// asynchronous execution!
FILESYS.readFile("./Stopping by Woods on a Snowy Evening.txt", function (error, data){
    if (error){
        console.error(error);
    }else{
        console.log(data.toString());
    }
});

// below code will be executed before the file reading finishes
console.log("This will be printed once the text file has been read!");
console.log("");

// function(error, data) is a callback function
// which is an asynchronous function, which will be executed once the previous operation i.e fileRead() is finished
// thus, w/o waiting Node executes the downstream code!
