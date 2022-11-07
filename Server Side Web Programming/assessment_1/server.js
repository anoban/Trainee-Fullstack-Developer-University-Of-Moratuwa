const EXPRESS = require("express");     // load in the express library
var WebApp = EXPRESS();     // instantiate the express library

const dataBase = require("./database.js");  // load in the user defined module
const bodyParser = require("body-parser");      // required to parse json text

const {request, response} = require("express");

WebApp.use(bodyParser.json());

let HTTP_PORT = 8080;
WebApp.listen(HTTP_PORT, function(){
    console.log(`Node.js server is listening at port :${HTTP_PORT}`);

});

// to deal with incoming post requests to the Node.js server and
// to write the received data to SQLite database
WebApp.post("/SQLiteAPI/customer", function(request, response, next){   
    // an API endpoint is specified here
    // assume this is the data user has provided that the server has to store in the database
    try{
    if(!request.body){
        console.log("Invalid POST request body!");
    }else{
        // capturing & unpacking the incoming post request body into following variables 
        console.log("An http POST request has been received by the Node server!")
        console.log("Processing the request...........")
    const {
        name,
        address,
        email,
        dateOfBirth,
        gender,
        age,
        cardHolderName,
        cardNumber,
        expiryDate,
        cvv,
        timeStamp
    } = request.body;
    
    // defining a SQL query template to append records to the database table "customer"
    var query =  `INSERT INTO customer (name, address, email, dateOfBirth, gender, age, cardHolderName, cardNumber, expiryDate, cvv, timeStamp) VALUES(?,?,?,?,?,?,?,?,?,?,?)`;
    // the question marks in the query are to be replaced by values captured from the post request
    var record = [name, address, email, dateOfBirth, gender, age, cardHolderName, cardNumber, expiryDate, cvv,
        timeStamp]; 
    // for testing successful reception & unpacking of the POST request body! commented out for now :(
    // console.log(record);   
        
    // data validation
    if (cardNumber.toString().length != 12){    // credit card number must be of 12 digits
        console.log(`Registration of user ${name} was rejected due to invalid credit card number!`)
        response.status(400).json({
            "message": "Invalid credit card number",
            "status":"Registration failed"
        });
    }else if (email.indexOf("@") == -1 || email.length < 10 || email.indexOf(".") == -1){   
        // dummy email address validation
        // addmittedly error prone :(
        /* assumes "@" is present in all email addresses, valid email addressess cannot be less than 10 
        characters in length & all valid email addresses should have at least one period in them */
        console.log(`Registration of user ${name} was rejected due to invalid email address!`)
        response.status(400).json({
           "message": "Invalid email address",
            "status": "Registration failed"
        });
    }else{  // this will be executed only if the data validation succeeds!
        dataBase.table.run(query, record, function(error, result){
        if(error){
            console.error(error);
            response.status(400).json({
                "error": error.message
            });
            return;
        }else{
            console.log(`A new record for customer ${name} has been created!`);
            response.status(201).json({
                "message": `Customer ${name} has registered!`,
                "customerId": this.lastID
            });
        }
    });
    }
}
}catch(Error){
    response.status(400).send(Error);
    // to identify where the error has occurred! commented out for now :/
    // console.error("This error was caught in the catch block!");
    console.error(Error.message);
}
});

