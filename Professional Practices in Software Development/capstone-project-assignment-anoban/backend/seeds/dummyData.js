exports.seed = function(knex) {
  return knex('dummyData').del()
    .then(function () {
      return knex('dummyData').insert([
        { id: 0000001, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
        { id: 0000002, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
        { id: 0000003, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
        { id: 0000004, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
        { id: 0000005, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
        { id: 0000006, dummyDataOne: 'DummyData', dummyDataOne: 'DummyData'},
      ]);
    });
};