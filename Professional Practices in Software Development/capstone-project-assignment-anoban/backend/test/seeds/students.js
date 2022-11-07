exports.seed = function(knex) {
  return knex('student').del()
    .then(function () {
      return knex('student').insert([
        { id: 20001, name: 'Supun Mihiranga', age: 10, hometown: 'Colombo'},
        { id: 20002, name: 'Sandun Perera', age: 9, hometown: 'Galle'},
        { id: 20003, name: 'Isuri De Silva', age: 10, hometown: 'Kandy'}
      ]);
    });
};