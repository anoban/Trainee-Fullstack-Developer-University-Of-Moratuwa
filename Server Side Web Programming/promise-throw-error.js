const PROMISE = new Promise(function(resolved, rejected){
    resolved("Promise has been resolved successfully!");
    rejected("Promise has failed!");
})
    .then(function(value){
        throw "We purposefully raised an error lol!";     // raises a dummy error, code below this line belonging to this method won't be executed!
        console.log(value);         // prints the output received from the PROMISE object
        return "A";     // returns "A" to the downstream .then() method!
    })
// the error raising will prevent the execution of code chunk below that line of code!
    .then(function(value){
        console.log(value);
        return "B";
    })
    .then(function(value){
        console.log(value);
        return "C";
    })
    .then(function(value){
        console.log(value);
        return "D";
    })
    .catch(function(error){
        console.log(error);
        console.log("and yes.. that's the error we raised!");
    })
