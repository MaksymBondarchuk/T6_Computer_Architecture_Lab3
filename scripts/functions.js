/**
 * Created by Maxim on 05.05.2015.
 */


function insertRowToTable(table, name, about, state) {
    var newRow = table.insertRow(0);
    var cellName = newRow.insertCell(0);
    cellName.innerHTML = name;
    var cellAbout = newRow.insertCell(1);
    cellAbout.innerHTML = about;
    var cellState = newRow.insertCell(2);
    cellState.innerHTML = state;
}


function read() {
    $.get("/read", function (data) {
        var labs = JSON.parse(data);
        var table = $("table")[0];
        //table.empty();

        while (table.rows.length > 0)
            table.deleteRow(0);

        for (var i = labs.length - 1; 0 <= i; i--) {
            var name = labs[i]['name'];
            var about = labs[i]['about'];
            var state = labs[i]['state'];
            insertRowToTable(table, name, about, state);
        }
        insertRowToTable(table, 'Name', 'About', 'State');


        var select = $("#nameChange")[0];

        while (select.length > 0)
            select.remove(select.length - 1);

        for (var j = 0; j < labs.length; j++) {
            var option = document.createElement("option");
            var nameOption = labs[j]['name'];
            option.value = nameOption;
            option.text = nameOption;
            select.add(option);
        }
    });
}