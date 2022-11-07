exports.up = function (knex) {
    return knex.schema
      .createTable("teacher", function (table) {
        table.increments("id").notNullable().primary();
        table.string("name", 255);
        table.int("age");
      })
      .createTable("student", function (table) {
        table.increments("id").notNullable().primary();
        table.string("name", 255);
        table.int("age");
        table.string("hometown", 255);
      })
      .createTable("dummyData", function (table) {
        table.increments("id").notNullable().primary();
        table.string("dummyDataOne", 255);
        table.string("dummyDataTwo", 255);
      })
  };
  
  exports.down = function (knex) {
    return knex.schema
      .dropTable("teacher")
      .dropTable("student")
      .dropTable("dummyData")
  };
  