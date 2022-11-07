const knex = require("knex")
const config = require("../knexfile")
const testBase = require("../backend/test/testBase");

let db = null
if (process.env.NODE_ENV === "test") {
  console.log("TEST DB")
  db = knex(config.test)
  testBase.resetDatabase(db);
} else if (process.env.NODE_ENV === "test-backend") {
  console.log("TEST DB")
  db = knex(config.test)
}else {
  console.log("DEV DB")
  db = knex(config.development)
}

module.exports = db