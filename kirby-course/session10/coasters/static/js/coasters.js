function delcoaster(the_coaster) {
    if (the_coaster.indexOf("*") !== -1){
        var display = the_coaster.replace("*", "'");
    } else  {
        var display = the_coaster;
    }
    var r = confirm("Delete " + display + "???");
    if (the_coaster.indexOf("*") !== -1){
        var seek = the_coaster.replace("*", "'");
    } else  {
        var seek = the_coaster;
    }
    if (r == true) {
        window.open('/delete/' + seek);
    } else {
        x = "You pressed Cancel!";
    }
}