/*
there are two types of errors!
1) programmer errors
2) operational errors

operational errors are runtime errors!
these occur mostly under the influence of external functions!
e.g. unable to connect to server/database, request timeout, invalid user input, system out of memory, socket hangup, file not found etc.. 
*/

/*
programmer errors are called bugs!
represent issues in the code!
e.g: array index out of bounds, syntax error, reference errors, failure to handle runtime errors, deprecation warnings etc... 
*/

// try catch
/*
try {
    // do something
} catch (error){
    // do this to resolve the error
    // error thrown in the try block is captured in the variable "error"
} 
*/


// error handling using try catch blocks
const FILESYS = require("fs");
console.log("Try block begins from here!");
try{
    var text = FILESYS.readFileSync("birches.txt"); // fs module's read calls are case insensitive to file names!
    console.log(text.toString());
    console.log("This is the end of try block!")
}
catch(error){
    console.log("Catch block begins here!")
    console.error(error);
}

console.log("------------------------------------------------------------------------------------");

// error handling using callbacks
var file = FILESYS.readFile("Acquainted with the Night.txt", function(error, data){
    if (error == null){
        console.log(data.toString());
    }else {
        console.error(error);
    }
}); 

console.log("--------------------------------------------------------------------------------------");

// error handling using promises
new Promise(function(resolved, rejected){
    FILESYS.readFile("Acquainted with the Night.txt", function(error, result){  // function call with callback
        if (result != null){
            console.log("File has been read succesfully!");        
            resolved(result.toString());    // resolved attribute of the promise
        }else if(error){
            console.log("File reading failed!");    
            rejected(error);    // rejected attribute of the promise
        }
    });
})  // this will return a new promise with a resolved & rejected attributes
.then(function(result){
    console.log(result);
},
    function(error){
        console.error(error);
});