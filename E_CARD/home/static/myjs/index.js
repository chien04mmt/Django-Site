//Show My application
function Show_My_Application() {
    var docno = 'all';
    var host = window.location.protocol + "//" + window.location.host;
    var hostname = window.location = host + "/querydoc/?userID=" + docno;
    window.location.assign(hostname);
    window.location = hostname;
    window.location.href = hostname;
    return false;
}

//Show My Sign application
function Show_My_SIGN_DOC() {
    var data = 'sign';
    var host = window.location.protocol + "//" + window.location.host;
    var hostname = window.location = host + "/querydoc/?datasign=" + data;
    window.location.assign(hostname);
    window.location = hostname;
    window.location.href = hostname;
    return false;
}