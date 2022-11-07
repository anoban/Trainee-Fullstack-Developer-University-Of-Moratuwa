const server = require("../server.js");
const supertest = require("supertest");
const requestWithSupertest = supertest(server);

const db = require("../db-config");
const testBase = require("./testBase");

beforeAll(async () => {
  await testBase.resetDatabase(db);
});

/**
 * Reset the database after every test case
 */
afterEach(async () => {
  await testBase.resetDatabase(db);
});

describe("Teacher Endpoints", () => {
  it("GET /listTeachers should show all teachers", async () => {
    const res = await requestWithSupertest.get("/listTeachers");
    expect(res.status).toEqual(200);
    let body = res.body;
    expect(body.length).toEqual(3);
    body.forEach(element => {
      expect(element).toHaveProperty('age');
      expect(element).toHaveProperty('name');
      expect(element).toHaveProperty('id');
    });

    expect(body[0].name).toBe('Kusuma Ranasinghe');
    expect(body[1].name).toBe('Saman De Silva');
    expect(body[2].name).toBe('Parasanna Mahagamage');
  });

  it("POST /addTeacher should show a newly added teacher", async () => {
    // add new teacher
    await requestWithSupertest.post("/addTeacher").send({
      "id": 10033,
      "name": "Nilanthi Fernando",
      "age": 42
    });

    const res = await requestWithSupertest.get("/listTeachers");
    expect(res.status).toEqual(200);
    let body = res.body;

    expect(body.length).toBe(4)

    expect(body).toContainEqual({
      "id": 10033,
      "name": "Nilanthi Fernando",
      "age": 42
    });
  });

  it("POST /editTeacher should show a newly added teacher", async () => {
    // add new teacher
    await requestWithSupertest.post("/editTeacher").send({
      "id": 10002,
      "name": "Saman",
      "age": 50
    });

    const res = await requestWithSupertest.get("/listTeachers");
    expect(res.status).toEqual(200);
    let body = res.body;

    expect(body).toContainEqual({
      "id": 10002,
      "name": "Saman",
      "age": 50
    });

    expect(body).not.toContainEqual({
      "name": "Saman De Silva",
    });
  });

  it("POST /deleteTeacher should delete a teacher", async () => {

    // delete Student
    await requestWithSupertest.post("/deleteTeacher").send({
      "id": 10003
    });

    const res = await requestWithSupertest.get("/listTeachers");
    expect(res.status).toEqual(200);
    let body = res.body;

    body.forEach(element => {
      expect(element).toHaveProperty('age');
      expect(element).toHaveProperty('name');
      expect(element).toHaveProperty('id');
    });

    expect(body.length).toBe(2);

    expect(body).toContainEqual({
      "id": 10001,
      "name": "Kusuma Ranasinghe",
      "age": 45
    });

    expect(body).not.toContainEqual({
      "id": 10003,
      "name": "Parasanna Mahagamage",
      "age": 30
    });
  });
});

describe("Student Endpoints", () => {
  it("GET /listStudents should show all students", async () => {
    const res = await requestWithSupertest.get("/listStudents");
    expect(res.status).toEqual(200);
    let body = res.body;
    expect(body.length).toEqual(3);
    body.forEach(element => {
      expect(element).toHaveProperty('age');
      expect(element).toHaveProperty('name');
      expect(element).toHaveProperty('id');
      expect(element).toHaveProperty('hometown');
    });

    expect(body[0].name).toBe('Supun Mihiranga');
    expect(body[1].name).toBe('Sandun Perera');
    expect(body[2].name).toBe('Isuri De Silva');
  });

  it("POST /addStudent should show a newly added student", async () => {
    // add new student
    await requestWithSupertest.post("/addStudent").send({
      "id": 99999,
      "name": "Rashini Shehara",
      "age": 12,
      "hometown": "Galle"
    });

    const res = await requestWithSupertest.get("/listStudents");
    expect(res.status).toEqual(200);
    let body = res.body;

    expect(body.length).toBe(4)

    expect(body).toContainEqual({
      "id": 99999,
      "name": "Rashini Shehara",
      "age": 12,
      "hometown": "Galle"
    });
  });

  it("POST /editStudent should edit a Student", async () => {
    // add new teacher
    await requestWithSupertest.post("/editStudent").send({
      "id": 20002,
      "name": "Sandakan",
      "age": 15,
      "hometown": "Homagama"
    });

    const res = await requestWithSupertest.get("/listStudents");
    expect(res.status).toEqual(200);
    let body = res.body;

    expect(body).toContainEqual({
      "id": 20002,
      "name": "Sandakan",
      "age": 15,
      "hometown": "Homagama"
    });

    expect(body).not.toContainEqual({
      "name": "Sandun Perera",
    });
  });

  it("POST /deleteStudent should delete a student", async () => {

    // delete Student
    await requestWithSupertest.post("/deleteStudent").send({
      "id": 20003
    });

    const res = await requestWithSupertest.get("/listStudents");
    expect(res.status).toEqual(200);
    let body = res.body;

    expect(body.length).toBe(2)

    body.forEach(element => {
      expect(element).toHaveProperty('age');
      expect(element).toHaveProperty('name');
      expect(element).toHaveProperty('id');
      expect(element).toHaveProperty('hometown');
    });

    expect(body).toContainEqual({
      "id": 20001,
      "name": "Supun Mihiranga",
      "age": 10,
      "hometown": "Colombo"
    });

    expect(body).not.toContainEqual({
      "id": 20003,
      "name": "Isuri De Silva",
      "age": 10,
      "hometown": "Kandy"
    });
  });
});
