const SQLite3 = require("sqlite3").verbose();       // load in the sqlite3 library

// database table where to store data & retrieve data from
const db_table = "table.sqlite";

let table = new SQLite3.Database(db_table, function(error){
    if(error){
        console.error(error.message);
        throw error;
    }else{
        console.log("Web application has successfully connected to the SQLite database!");
        // following code executes in the database to vreate a database table named "PRODUCTS"
        table.run(
            `CREATE TABLE PRODUCTS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCT_NAME TEXT,
            DESCRIPTION TEXT,
            CATEGORY TEXT,
            BRAND TEXT,
            EXP_DATE TEXT,
            MFDATE TEXT,
            BATCH_NUMBER INTEGER,
            UNIT_PRICE INTEGER,
            QUANTITY INTEGER,
            CREATED_DATE TEXT)`), function(error){
            if(error){
                console.error(error);
                console.log("Table has already been created!");
            }else{
                // table has just been created, creating a row
                var query = `INSERT INTO PRODUCTS (PRODUCT_NAME, DESCRIPTION, CATEGORY, BRAND, EXP_DATE, MFDATE, BATCH_NUMBER, UNIT_PRICE, QUANTITY, CREATED_DATE) VALUES(?,?,?,?,?,?,?,?,?,?)`;
                // execute the above query with following data
                table.run(query, ["Dell laptop", "Dell Latitude i234", "Computers", "Dell", "None", "12-09-2021", 321, 230000, 43, "24-11-2021"]);
            }
        }
    }
});