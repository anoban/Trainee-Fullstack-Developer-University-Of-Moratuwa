// a third party module
const fetch = require("node-fetch");

const url = "https://my-json-server.typicode.com/typicode/demo/comments";

// fetch() retrieves data from external resources and returns a promise object
// usnig promises but not async & await
fetch(url)
.then(function(response){
    return response.json();
})
.then(function(data){
    console.log(data);
})
.catch(function(error){
    console.log(error);
})

/*
received two json objects
[
  { id: 1, body: 'some comment', postId: 1 },
  { id: 2, body: 'some comment', postId: 1 }
]
*/


// using async & await
//create an async function
const retrieve = async function(){
    const url = "https://my-json-server.typicode.com/typicode/demo/comments";
    try {
        const response = await fetch(url);  // await makes the programme to wait until the execution of this line finishes!
        const data = await response.json();
        return data;
    }
    catch(error){
        console.log(error);
    }
};

retrieve()
.then(function(value){
    console.log(value)
},
function(error){
    console.log(error);
});
