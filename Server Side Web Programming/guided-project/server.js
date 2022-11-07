const EXPRESS = require("express");     // load in the express library
var WebApp = EXPRESS();     // initialize the express library

const dataBase = require("./database.js");  // a user defined module
const bodyParser = require("body-parser");      // required to parse json data

const {request, response} = require("express");

WebApp.use(bodyParser.json());

let HTTP_PORT = 8080;

WebApp.listen(HTTP_PORT, function(){
    console.log(`Node.js server is listening at port :${HTTP_PORT}`);
});

// to send data to SQLite database
WebApp.post("/SQLiteAPI/products", function(request, response, next){   // an API endpoint is specified here
    // assume this is the data user has provided that the server has to store in the database
    try{
        var errArray = [];
    if(!request.body){
        errArray.push("An invalid input!");
    }
    const {
        PRODUCT_NAME,
        DESCRIPTION,
        CATEGORY,
        BRAND,
        EXP_DATE,
        MFDATE,
        BATCH_NUMBER,
        UNIT_PRICE,
        QUANTITY,
        CREATED_DATE
    } = request.body;
    var query =  `INSERT INTO PRODUCTS (PRODUCT_NAME, DESCRIPTION, CATEGORY, BRAND, EXP_DATE, MFDATE, BATCH_NUMBER, UNIT_PRICE, QUANTITY, CREATED_DATE) VALUES(?,?,?,?,?,?,?,?,?,?)`;
    // these question marks in the queries are to be replaced by real values in execution time
    var columns = [PRODUCT_NAME, DESCRIPTION, CATEGORY, BRAND, EXP_DATE, MFDATE, BATCH_NUMBER, UNIT_PRICE, QUANTITY, CREATED_DATE];
    
    dataBase.run(query, columns, function(error, result){
        if(error){
            response.status(400).json({
                "error":error.message
            });
            console.error(error.message);
            return;
        }else{
            response.json({
                "message":"Success",
                "data":response.body,
                "ID":this.lastID
            })
        }
    });
} catch(Error){
    response.statusCode(400).send(Error);
}
});

// to get data from the SQLite database
WebApp.get("/SQLiteAPI/products", function(request, response, next){
    try{
       var query = `SELECT * FROM PRODUCTS ` ;
    var columns = [];
    dataBase.all(query, columns, function(error, rows){
        if(error){
            response.status(400).json({"error":error.message});
        }else{
            response.json({
                "data":rows,
                "message":"Success"
            });
        }
    }); 
    }catch(Error){
        response.status(400).send(Error);
    }    
});

// defining a put method
WebApp.put("/SQLiteAPI/products", function(request, response, next){   // an API endpoint is specified here
    // assume this is the data user has provided that the server has to store in the database
    try{
        var errArray = [];
    if(!request.body){
        errArray.push("An invalid input!");
    }
    const {
        PRODUCT_NAME,
        DESCRIPTION,
        CATEGORY,
        BRAND,
        EXP_DATE,
        MFDATE,
        BATCH_NUMBER,
        UNIT_PRICE,
        QUANTITY,
        CREATED_DATE
    } = request.body;
    var query =  `UPDATE PRODUCTS SET PRODUCT_NAME = ?, DESCRIPTION = ?, CATEGORY = ?, BRAND = ?, EXP_DATE = ?, MFDATE = ?, BATCH_NUMBER = ?, UNIT_PRICE = ?, QUANTITY = ?, CREATED_DATE = ? WHERE ID = ?`;
    // these question marks in the queries are to be replaced by real values in execution time
    var columns = [PRODUCT_NAME, DESCRIPTION, CATEGORY, BRAND, EXP_DATE, MFDATE, BATCH_NUMBER, UNIT_PRICE, QUANTITY, CREATED_DATE];
    
    dataBase.run(query, columns, function(error, result){
        if(error){
            response.status(400).json({
                "error":response.message
            });
            return;
        }else{
            response.status(200).json({"Updated":this.changes})
        }
    });
} catch(Error){
    response.statusCode(400).send(Error);
}
});


// delete method
WebApp.delete("/SQLiteAPI/products/delete:id", function(request, response, next){
    try{
    dataBase.run("DELETE FROM PRODUCTS WHERE ID = ?", request.columns.id, function(error, result)
    if(error){
        response.status(400).json({"error":response.message})
        return;
    }else{
        response.json({"message":"deleted",
                      "rows":this.changes})
    });    
    }catch(Error){
        response.status(400).send(Error);
    }
});