/**
 * Created by Maxim on 05.05.2015.
 */

function initial() {
    alert('File loaded');
}


function read() {
    $.get("/read", function(data){
        data = JSON.parse(data);
        alert(data);
    });

    //$.get('/read', function (data) {
    //        var table = $.('#table')[0];
            //var data1 = JSON.parse(data);
            //alert(data);
        //}
    //);
}