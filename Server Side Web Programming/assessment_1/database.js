const SQLite3 = require("sqlite3").verbose();       // load in the sqlite3 library

// a local SQLite database where to store data & retrieve data from
const dbase = "SQLiteDB";

// create a SQLite database table
let table = new SQLite3.Database(dbase, function(error){
    if(error){
        console.error(error.message);
        throw error;
    }else{
        console.log("Web application has successfully connected to the SQLite database!");
        // following query executes in the database to create a database table named "customer"
        // age, cardNumber & cvv were all given as strings in the example but...
        table.run(
            `CREATE TABLE customer(
            customerId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            email TEXT,
            dateOfBirth TEXT,
            gender TEXT,
            age INTEGER,
            cardHolderName TEXT,
            cardNumber INTEGER,
            expiryDate TEXT,
            cvv INTEGER,
            timestamp TEXT)`), function(error, data){
            if(error){
                // if a table named "customer" already exists in the database
                console.error(error);
                console.log("Table with the requested name already exists in the database!");
            }else{
                // table has just been created
                console.log("Table has just been created!");
            }
        }
    }
});

module.exports = {table};