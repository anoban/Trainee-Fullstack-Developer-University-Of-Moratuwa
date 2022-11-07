import { Selector } from 'testcafe';
process.env.NODE_ENV = "test";

fixture`Testing Student UI`
    .page`http://localhost:4401/student`

test('Testing delete students', async t => {
    await t.navigateTo("/addStudent");
    await t.typeText("#student-id", "222222");
    await t.typeText("#student-name", "Hiruni Gajanayake");
    await t.typeText("#student-age", "45");
    await t.typeText("#student-Hometown", "buddhist");
    await t.click("#student-add");

    await t.navigateTo("/student");

    await t.click("#student-delete-222222");

    const table = Selector('#student-table')
    const rowCount = await table.find('tr').count;

    let tdText = await table.find('tr').nth(rowCount - 1).innerText;
    await t.expect(tdText).notContains("Hiruni Gajanayake");
});