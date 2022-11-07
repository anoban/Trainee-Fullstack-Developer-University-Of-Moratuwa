## 2. Implementing the Backend

Implementing the Backend can be divided into 3 parts.

1. [Creating the functions to interact with the Database](#21-creating-the-functions-to-interact-with-the-database).
2. [Creating the Backend server](#22-creating-the-backend-server).
3. [Starting the server](#23-starting-the-server)

Since, we successfully added the dummy data during the [Setting up the environment](/docs/chapters/setting-up-the-environment.md) section, let's initialize the database using the `configuration` file provided.

```javascript
const dbConnection = require("./sqlite");

dbConnection
  .getDbConnection()
  .then((db) => {
    init(db);
  })
  .catch((err) => {
    console.log(err);
    throw err;
  });

let _db;

function init(db) {
    _db = db;
}

const knex_db = require("./db-config");
```

- Using the `sqlite.js` file provided inside the **backend** folder, we import methods from it as `dbConnection`. Then, by using the `getDbConnection` method which is exported in the module, we initialize a database connection and assign it to the `_db` variable.
- Then the `Knex` module, which is a `SQL Query Builder` will establish a connection to this database using the configuration given at `db-config.js`.  

Now, let's create the methods for the `CRUD operations` related to the `teacher` class.

> Here, `CRUD operations` refers to `Create`, `Read`, `Update`, and `Delete` operations of the data.

### 2.1. Creating the functions to interact with the Database

In this tutorial we will be guiding you to creating the functions for the `CRUD operations` of the teacher class.

#### First let's create the function for adding a teacher to the database.

```js
const addTeacher = async (id, name, age) => {
    const sql = `INSERT INTO teacher(id,name,age) values (?, ?, ?)`
    return new Promise((resolve, reject) => {
        knex_db
            .raw(sql, [id, name, age])
            .then(() => {
                resolve({status: "Successfully inserted Teacher"})
            })
            .catch((error) => {
                reject(error);
            });
    });
}
```

- Here a `Promise` is returned when a `teacher` object is created. A `Promise` object represents the eventual completion (or failure) of an asynchronous operation and its resulting value [[1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)]. A function can be passed into the `Promise` object with `resolve`, and `reject` methods to be called upon successfully completion or failure respectively.
- In the above code, when a teacher is successfully added to the database, the `resolve` method will return a `status` message as `"Successfully added teacher"`. If any error is occurred during the creation of a teacher, the `reject` method will return the details of the `error` generated.
- The SQLite query of the form `INSERT INTO <table_name> (attribute_1, attribute_2, ...) VALUES (value_1, value_2, ...)` is used to insert data to a table in the database. Here, the values will be inserted into the table in the order the attributes are specified in the query.
- The `raw` method of the `Kenx.js` accepts a raw SQL query. To prevent [SQL injection](https://www.w3schools.com/sql/sql_injection.asp) a parameterized query is used. The **Positional Bindings** `?` are interpreted as `values` and `??` are interpreted as `identifiers` in `Knex.js`. The values and identifiers passed as an `array` to the `raw` method will replace the **Positional Bindings** and complete the query string.

#### Secondly let's create the function for Reading the Information of the teachers in the database.

> Let's look at the database function to read/retrieve the teacher data from the database.

```js
const readTeachers = async () => {
    const sql = `SELECT * FROM teacher`
    return new Promise((resolve, reject) => {
        knex_db
            .raw(sql)
            .then((teachers) => {
                resolve(teachers);
            })
            .catch((error) => {
                reject(error);
            });
    });
}
```

- In the above code, all the teacher information in the teacher table is retrieved. The `resolve` method will return the database rows of the teacher table. If any error is occurred during the creation of a teacher, the `reject` method will return the `error` details.
- The SQLite query of the form `SELECT * FROM <table_name>` is used to retrieve all the data of a table in the database. Here, `*` is used to retrieve data of all the columns. Alternatively we can specify the column names of which the data should be retrieved.

#### Implementation of retrieving a single teacher object.

```js
const readTeacherInfo = async (id) => {
    const sql = `SELECT * FROM teacher WHERE id = ?`
    return new Promise((resolve, reject) => {
        knex_db
            .raw(sql, [id])
            .then((teacher) => {
                resolve(teacher);
            })
            .catch((error) => {
                reject(error);
            });
    });
}
```

- The `readTeacherInfo` method accepts an `id` parameter which is referring to the **teacher's id**.
- The `id` parameter is then used in the SQLite query with a `WHERE` clause to filter the specified teacher among all teachers.
- Similarly, if an error occurs it is returned via `reject` method and if not the resulting `rows` are returned via `resolve`.

#### Next, let's create a function to update the details of a teacher.

```javascript
const updateTeacher = async (name, age, id) => {
    const sql = `UPDATE teacher SET name=?, age=? WHERE id=?`
    return new Promise((resolve, reject) => {
        knex_db
            .raw(sql, [name, age, id])
            .then(() => {
                resolve({status: "Successfully updated Teacher"})
            })
            .catch((error) => {
                reject(error);
            });
    });
}
```

- The SQLite query format `UPDATE <table_name> SET attribute_1=value_1, attribute_2=value_2 WHERE id_1=id_value_1, id_2=_id_value_2, ...` is used to update an existing record in the table. Here, we us it to update a details of a teacher.

#### Finally, let's implement the function for the delete operation of the teacher class.

```js
const deleteTeacher = async (id) => {
    const sql = `DELETE FROM teacher WHERE id = ?`
    return new Promise((resolve, reject) => {
        knex_db
            .raw(sql, [id])
            .then(() => {
                resolve({status: "Successfully deleted Teacher"})
            })
            .catch((error) => {
                reject(error);
            });
    });
}
```

- In SQLite, the SQLite query format `DELETE FROM <table_name> WHERE <attribute_1>=<value_1> AND/OR ...` is used for deleting a row from the given table. In the above code the `teacher's id` value is used to identify the row to be deleted from the `teacher` table.

After implementing the `database functions`, we need to `export` them to make sure that other modules have access to them. This can be done via the `module.exports` object.

```javascript
module.exports = {
    addTeacher,
    readTeachers,
    readTeacherInfo,
    updateTeacher,
    deleteTeacher
}
```

### 2.2. Creating the Backend server

In this section, we will be learning how the `Backend Server` is implemented.

#### Importing the essentials to run our Backend server.

```js
import express from "express";
import bodyParser from "body-parser";
import {
    initializeDatabase,
    readTeachers,
    readTeacherInfo,
    addTeacher,
    deleteTeacher,
} from "./database.js";
```

- `Express` is a Node.js framework that provides facilities to run the services we need to initiate the server. We will be implementing APIs using `express` and the functions we created in [last section](#21-creating-the-functions-to-interact-with-the-database). Express provides a robust set of features for web application creation.
- Middlewares are functions that have access to the  `request object` (req), the `response object` (res), and the next function in the application’s `request-response cycle`. Middlewares are mainly used to reformat request object, response object or handle multimedia request (check on [Multer](https://www.npmjs.com/package/multer) for more information).
- The next import is the [`body-parser`](https://www.npmjs.com/package/body-parser). It is a Node.js middleware which will parse the incoming request bodies before getting to the handlers. This is essential for validating the inputs received before the request proceeds and also convert the request body into JS datatype. Read more about [body-parser](https://www.npmjs.com/package/body-parser).
- The next set of imports are the functions we created in the `database.js` file which contains the functions we created and described above. In JavaScript and in many other programming languages the functions defined in a different file should be imported first before using this in another file. A such code containing file is called a Module. Read more about [Modules](https://www.freecodecamp.org/news/javascript-modules-explained-with-examples/#:~:text=A%20module%20in%20JavaScript%20is,object%20accessible%20to%20other%20modules).

```js
const app = express();
```

- This creates the express framework object which is used to initialize our server. Read more on [express()](https://expressjs.com/en/api.html).

```js
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
```

- In this [app.use()](https://expressjs.com/en/guide/using-middleware.html) instructs the express object to use the middlewares passed as parameters. The first middleware passed is the [bodyparser.urlencoded()](http://expressjs.com/en/resources/middleware/body-parser.html) which Returns middleware that only parses urlencoded bodies and [bodyparser.json()](http://expressjs.com/en/resources/middleware/body-parser.html) instructs the request body should be in the json format.

#### Next step is to create APIs using the functions we created in the last section.

##### 1. API for retrieving teachers
```js
app.get("/listTeachers", async function (req, res) {
    console.log("Request received to list teachers");
    let data = await readTeachers();
    
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify(data));
});
```

- This is the API for retrieving the list of teachers using the `readTeachers` function.

> Depending on what we need to do with an API, different methods are used to send requests to the APIs. Following are the most commonly used methods.
> 1. `POST` - This method is used when an API is used to send data (*create*).
> 2. `GET` - This method is used when an API is used to retrieve data (*read*).
> 3. `PUT` - This method is used when an API is used to update already existing data (*update*).
> 4. `DELETE` - This method is used when an API is used to delete data (*delete*).
>
> As mentioned in the parentheses, these methods map to the `CRUD` operations.

- In the `express` module, we pass a `path` argument and a `callback` function to the `get` method. Here the `path` refers to the endpoint we will be using to call the API. The `callback` function contains a `Request` and a `Response` object which is denoted by `req` and `res` respectively. Those objects contain methods to manipulate the request and the response of the API. For further details, access the documentation of `express` using this [link](https://expressjs.com/).
- In the above example, the `readTeachers` API is accessed through a `get` method. The endpoint `/listTeachers` is used to direct the requests to the API.
- Note that an `async` function is used for the callback function. An `async` function are used to return a `Promise`. In the [section](#secondly-lets-create-the-function-for-reading-the-information-of-the-teachers-in-the-database) when we created the `readTeachers` function, note that a `Promise` is returned. To return this `Promise` value, an `async` function is used as the callback function of the `get` method. To access the `Promise` value, an `await` statement is used. This stops the execution of the function until the returned `Promise` is resolved or rejected.
- Finally, `res.setHeader()` is used to set the header values of the response, and `res.end()` is used to end the response process. For further details about the methods, use this [link](https://expressjs.com/en/5x/api.html#res).

#### 2. API for retrieving a single teacher

```js
app.post("/getTeacherInfo", async function (req, res) {
  let reqBody = req.body;
  console.log("Request received to get Teacher Info");
  let data = await readTeacherInfo(reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});
```

- Using the above API we can get the information of a particular teacher identified through the teacher's id.
- This API is accessed through the URL `/getTeacherInfo` via a `post` request. The data required to identify the teacher (*teacher's id*) is passed as a javascript object in the following format.

```json
{
  "id": "teacher_id"
}
```

- This incoming data object can be captured by the `body` attribute of the `req` object.
- By triggering this API, a teacher with the specified `teacher_id` will be returned.

##### 3. API for adding/creating a teacher

```js
app.post("/addTeacher", async function (req, res) {
    let reqBody = req.body;
    console.log(
    "Request received to add teacher. Req body: " + JSON.stringify(reqBody)
    );
    let data = await addTeacher(reqBody.id, reqBody.name, reqBody.age);
    
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify(data));
});
```

- This is the API for creating/adding a teacher to the database via the `addTeacher` method we created earlier.
- Similar to the previous API, this API uses the endpoint `/addTeacher` to access the API via a `post` method/request. The data required to create the teacher object is passed to the `post` method as a javascript object in the following format.

```json
{
  "id": "teacher_id",
  "name": "teacher_name",
  "age": "teacher_age"
}
```

- By triggering this API, a teacher object will be created in the database with the specified details in the data object of the request.

##### 4. API for deleting a teacher

```js
app.post("/deleteTeacher", async function (req, res) {
    let reqBody = req.body;
    console.log(
    "Request received to delete teacher. Req body: " + JSON.stringify(reqBody)
    );
    let data = await deleteTeacher(reqBody.id);
    
    res.setHeader("Content-Type", "application/json");
    res.end(JSON.stringify(data));
});
```

- This API is used to delete a `teacher` object from the database using the `teacher's id` specified in the body of the `post` request.
- Similar to the above APIs, the endpoint `/deleteTeacher` is used via a `post` method/request to delete the teacher object. The `teacher's id` is passed in the data object of the request in the following format as a javascript object.

```json
{
  "id": "teacher_id"
}
```

- This will pass the `id` value to the `deleteTeacher` method, and eventually it will delete the teacher object from the database with the specified `id` value.

##### 5. API for updating a teacher

```javascript
app.post("/editTeacher", async function (req, res) {
  let reqBody = req.body;
  let data = await updateTeacher(reqBody.name, reqBody.age, reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});
```

- This API is used to update the details of a `teacher` object using the `teacher's id` via a `post` request.
- By passing the relevant `data` to the `/editTeacher` endpoint via a `post` request, the details of specified teacher will be updated. The `data` object passed to the API will take the following format.

```json
{
  "name": "teacher_name",
  "age": "teacher_age",
  "id": "teacher_id"
}
```

After implementing the APIs, we need to export the `express app` to make sure other modules can access it. This can be done similary to how we exported the `database functions` in the [above section](#21-creating-the-functions-to-interact-with-the-database).

```javascript
module.exports = app;
```

### 2.3. Starting the server.

- When we check the `index.js` file we will the following code snippet

```js
import server from "./server.js";

server.listen(8080, function () {
  console.log(
    "Capstone Project Backend is running on http://localhost:8080"
  );
});
```

- Running this will activate the express server in port `8080` and you can send requests to this url.
- Read more on [server.listen()](https://www.geeksforgeeks.org/node-js-server-listen-method/).
- To run the Backend server, in the `project's root` open a terminal and run the following command.

```bash
npm start
```

> If you need to stop the server from running press,
> 1. Windows: `CONTROL` + `C`.
> 2. Mac: `COMMAND` + `C`.