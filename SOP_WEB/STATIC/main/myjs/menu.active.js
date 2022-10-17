// class="pcoded-hasmenu active pcoded-trigger"
//Xóa bỏ toàn bộ active của các menu
function REMOVE_ACTIVE_ALL_MENU() {
    $("ul").removeClass("active pcoded-trigger");
    $("li").removeClass("active");
}

//Active một menu trái
function ACTIVE_MENUX(el) {
    REMOVE_ACTIVE_ALL_MENU();
    $(el).addClass('active');
    $(el).parent('ul').parent('li').addClass('active pcoded-trigger');
}



//Active một menu trái
function ACTIVE_MENUY(element) {
    REMOVE_ACTIVE_ALL_MENU();
    $(element)
        .addClass('active')
        .parent('ul').parent('li').addClass('active pcoded-trigger');
}