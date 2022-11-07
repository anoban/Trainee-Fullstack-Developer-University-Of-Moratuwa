exports.seed = function(knex) {
    return knex('teacher').del()
      .then(function () {
        return knex('teacher').insert([
          { id: 10001, name: 'Kusuma Ranasinghe', age: 45},
          { id: 10002, name: 'Saman De Silva', age: 40},
          { id: 10003, name: 'Parasanna Mahagamage', age: 30}
        ]);
      });
  };