const express = require ("express");

const {
  readTeachers,
  readStudents,
  addStudent,
  addTeacher,
  deleteTeacher,
  deleteStudent,
  readStudentInfo,
  readTeacherInfo,
  updateStudent,
  updateTeacher,
  dbinitialize
} = require ("./database.js");

const app = express();
const bodyParser = require  ("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/dbinitialize", async function (req, res) {
  console.log("DB is getting initialized");
  let data = await dbinitialize();

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});
// ============== Teacher Related endpoints ==============

app.get("/listTeachers", async function (req, res) {
  console.log("Request received to list teachers");
  let data = await readTeachers();

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/getTeacherInfo", async function (req, res) {
  let reqBody = req.body;
  console.log("Request received to get Teacher Info");
  let data = await readTeacherInfo(reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/addTeacher", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to add teacher. Req body: " + JSON.stringify(reqBody)
  );
  let data = await addTeacher(reqBody.id, reqBody.name, reqBody.age);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/editTeacher", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to update teacher. Req body: " + JSON.stringify(reqBody)
  );
  let data = await updateTeacher(reqBody.name,reqBody.age,reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/deleteTeacher", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to delete teacher. Req body: " + JSON.stringify(reqBody)
  );
  let data = await deleteTeacher(reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

// ============== Student Related endpoints ==============

app.get("/listStudents", async function (req, res) {
  console.log("Request received to list students");
  let data = await readStudents();

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/getStudentInfo", async function (req, res) {
  let reqBody = req.body;
  console.log("Request received to get Student Info");
  let data = await readStudentInfo(reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/addStudent", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to add student. Req body: " + JSON.stringify(reqBody)
  );
  let data = await addStudent(
    reqBody.id,
    reqBody.name,
    reqBody.age,
    reqBody.hometown
  );

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/deleteStudent", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to delete student. Req body: " + JSON.stringify(reqBody)
  );
  let data = await deleteStudent(reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

app.post("/editStudent", async function (req, res) {
  let reqBody = req.body;
  console.log(
    "Request received to update Student. Req body: " + JSON.stringify(reqBody)
  );
  let data = await updateStudent(reqBody.name,reqBody.age,reqBody.hometown,reqBody.id);

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(data));
});

module.exports = app;