//Hiển thị thông tin chi tiết đơn vào form docdetail
function Doc_Detail(el) {
    var docno = $(el).text();
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/detail_bus/?docno=' + docno
        // window.open(newhref, '_blank'); //Mở 1 tab mới
        // window.open(newhref);
    window.location = newhref;
}