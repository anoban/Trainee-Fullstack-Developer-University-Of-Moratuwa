/* A Promise is in one of these states:
    pending: initial state, neither fulfilled nor rejected.
    fulfilled: meaning that the operation was completed successfully.
    rejected: meaning that the operation failed.

    Chaining of promises!
    Promise.prototype.then(), Promise.prototype.catch(),
    and Promise.prototype.finally() are used to associate further action with a promise that becomes settled.
    when a promise in not pending i.e fulfilled or rejected it is said to be resolved!.
    .then() method can be used in both cases of fullfilment & rejection!
    .catch() method is used upon rejection!
    .finally() method will be executed regardless of the promise state!
    similar to Python's try, except & finally block!
*/

// Promise() is a constructor!
const PROMISE = new Promise(function (resolved, rejected){   // Promises take two params; resolved, rejected
    resolved("Success!");       // fullfilment
    rejected("Failed!");        // rejection
});

PROMISE
    .then(function (value) {
        console.log(value);     // executed upon fullfilment
    })
    .catch(function (error){
        console.log(error);     // executed upon failure
    });
