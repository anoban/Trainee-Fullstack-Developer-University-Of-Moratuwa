// this is not equivalent to a promise that has both resolved & rejected functions defined!
// this is a shortcut to generate an instance of resolved promise!

const promise = Promise.resolve("Resolved promise!");        // will return "Resolved promise!"

const promise_1 = promise.then(function(value){
        console.log(value);
        return "Next resolved promise";
    });

const promise_2 = promise_1.then(function(value){
    console.log(value);
    return "Ahh another resolved promise!";
});

const rejected_promise = promise_2.then(function(value){
    console.log("Introducing an artificial error!");
    throw "An intentionally raised error!";
    console.log(value);
    return "This line won't be executed anyways lol!";
});

const promise_3 = rejected_promise.then(function(value){
    console.log(value);
    return "This line won't be executed since this is a callback for resolved promise!";
},
function(error){
    console.log(error);
    console.log("This line was executed since this is a callback for rejected promise!")
});
