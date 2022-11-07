const PROMISE = new Promise(function (resolved, rejected){
    resolved("The promise has been fullfilled!");
    rejected("The promise has been rejected!");
});


PROMISE
    .then(function(value){      // we are not defining a callback for rejection in the .then() method!
        console.log(value);
        return "A";
    })
    .then(function(value){     // the result of previous block in the chain will be passed as input for the downstream .then() block
        console.log(value);     // i.e value = "A"
        return "B";
    })
    .then(function (value){
        console.log(value);
        return "C";
    })
    .then(function(value){
        console.log(value);
        return "D";
    })
    .then(function(value){     // callback for handling resolved promise!
        console.log(value);
        console.log("No errors occurred!");
    },
    function(error){        // callback for handling rejected promise!
        console.log(error);
        console.log("An error has occurred!");
    });
