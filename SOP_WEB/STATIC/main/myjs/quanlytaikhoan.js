//Nhấn nút tìm kiếm User
function Search_User() {

    var data = GET_ALL_INPUT_FROM_DIV('search_div');

    $.ajax({
        type: 'GET',
        url: "/showsearchinfo/",
        data: data,
        success: function(response) {
            $("#tbody_Viewuser").empty();
            var ojb = response["returndata"];
            var num = 1;
            ojb.forEach(function myFunctionx(item, index1) {
                $("#tbody_Viewuser").append(
                    '<tr class="clickable-row">\
                    <td>' + num + '</td>\
                    <td style="color:Blue;text-decoration:underline;cursor:pointer" onclick="Load_AcountInfo(this.id.substring(this.id.indexOf(' + "'_'" + ')+1))" id="UserID_' + item['TenDangNhap'] + '">' + item['TenDangNhap'] + '</td>\
                    <td>' + item['HoTen'] + '</td>\
                    <td>' + item['SoDienThoai'] + '</td>\
                    <td class="text-left">' + item['Email'] + '</td>\
                    <td class="text-center" data-i18n="' + item['CodeRole'] + '">' + (!item['Name'] ? '' : item['Name']) + '</td>\
                    <td class="text-center">\
                        <i id="btnResetUs_' + item['TenDangNhap'] + '" class="fas fa-sync-alt fa-spin text-success" data-toggle="tooltip" data-placement="right" title="Reset Password" style="cursor: pointer;" onclick="ResetPassword(this)"></i><i class="fas ">&nbsp;||&nbsp;</i>\
                        <i id="btnEditUs_' + item['TenDangNhap'] + '" class="fas fa-edit text-info" data-toggle="tooltip" data-placement="right" title="Edit User" style="cursor: pointer;" onclick="Load_AcountInfo(this.id.substring(this.id.indexOf(' + "'_'" + ')+1))"></i><i class="fas ">&nbsp;||&nbsp;</i>\
                        <i id="btnDelUs_' + item['TenDangNhap'] + '" class="fas fa-trash-alt text-danger" data-toggle="tooltip" data-placement="right" title="Delete User" style="cursor: pointer;" onclick="DELETE_USER(this)"></i>\
                    </td>\
                </tr>');
                num += 1;
            });
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}



//Load danh sách phòng ban
function Load_Dept() {
    $.ajax({
        type: 'GET',
        url: '/load_department/',
        data: '',
        success: function(response) {
            $("#group_Dept").empty();
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#group_Dept").append(
                    '<div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12 mb-0 mt-0">\
                        <div class="form-check form-check-inline">\
                            <input class="form-check-input" type="checkbox" id="' + item['CatCode'] + '" value="' + item['CatCode'] + '">\
                            <label class="form-check-label" for="' + item['CatCode'] + '"  data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</label>\
                        </div>\
                    </div>');
            });
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Load danh sách chức vụ 
function Load_Permiss_Group() {
    $.ajax({
        type: 'GET',
        url: '/load_permissgroup/',
        data: '',
        success: function(response) {
            $("#group_permiss").empty();
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#group_permiss").append(
                    '<div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12 mb-0 mt-0">\
                        <div class="form-check form-check-inline">\
                            <input class="form-check-input" type="checkbox" id="' + item['CatCode'] + '" value="' + item['CatCode'] + '">\
                            <label class="form-check-label" for="' + item['CatCode'] + '"  data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</label>\
                        </div>\
                    </div>');
            });
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Load danh sách chủ quản phòng
function Load_Manager_room() {
    $.ajax({
        type: 'GET',
        url: '/load_manager_room/',
        data: '',
        success: function(response) {
            $("#select_manager").empty();
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#select_manager").append(
                    '<li class="select-multi select-choice">\
                        <span>' + item['Username_Manager'] + '_' + item['HoTen'] + '</span>\
                        <i class="fa-del text-danger" onclick="this.parentElement.remove()">×</i>\
                    </li>');
            });
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Load danh sách chủ quản phòng
function Load_List_Manager_room() {
    $.ajax({
        type: 'GET',
        url: '/load_listmanager_room/',
        data: '',
        success: function(response) {
            $("#myDropdown_Manager_list").empty();
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#myDropdown_Manager_list").append(
                    '<a class="dropdown-item" href="#" data-toggle="tooltip" data-placement="left" title="" data-original-title="" onclick="Choice_manager(this)">\
                        <i class="fa fa-user f-14 text-info" aria-hidden="true"></i> <span>' + item['UserName'] + '_' + item['HoTen'] + '</span></a>');
            });
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//Chọn chủ quản phòng từ menu
function Choice_manager(element) {
    $("#select_manager").append('<li class="select-multi select-choice"><span>' + $(element).text() + '</span> <i class="fa-del text-danger" onclick="$(this).parent().remove()">×</i></li>');
}



//tải thông tin tài khoản từ server ra bảng modal chi tiết người dùng
function Load_AcountInfo(TenDangNhap) {
    // console.log(TenDangNhap);

    $("#modaledituser :input").each(function() {
        $(this).prop('checked', false);
    });
    $("#select_manager").empty();
    $("#div_btnCreate").prop('hidden', true);
    $("#Div_pass1").prop('hidden', true);
    $("#Div_pass2").prop('hidden', true);
    $("#Div_None").prop('hidden', true);
    $("#div_btnUpdate").removeAttr('hidden');

    $.ajax({
        type: 'GET',
        url: '/show_tendangnhapInf/',
        data: { TenDangNhap: TenDangNhap },
        success: function(response) {
            var oject = response['returndata'];
            // console.log(oject);
            //Hiển thị thông tin tài khoản
            BINDING_DATA_TO_ID(oject['sql1'][0]);
            if (oject['sql1'][0]['DCC'] == true) { $("#DCC").prop("checked", true); }
            //Hiển thị quản lý phòng
            try {
                oject['sql4'].forEach(function FILL_DATA(item, index) {
                    $("#select_manager").append(
                        '<li class="select-multi select-choice">\
                            <span>' + item['Username_Manager'] + '_' + item['HoTen'] + '</span>\
                            <i class="fa-del text-danger" onclick="$(this).parent().remove()">×</i>\
                        </li>');
                });
            } catch (er) {}

            //Hiển thị chức vụ
            try {
                oject['sql3'].forEach(function FILL_DATA(item, index) {
                    $("#" + item['Position']).prop("checked", true);
                });
            } catch (er) {}

            //Hiển thị phòng ban trực thuộc
            try {
                oject['sql2'].forEach(function FILL_DATA(item, index) {
                    $("#" + item['Department']).prop("checked", true);
                });
            } catch (er) {}
            $("#modaledituser").modal('show');
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Sự kiện thay đổi select quyền hạn
function Change_select_Permiss(element) {
    if ($(element).val() == 'R-00022') { $("#DCC").prop('checked', true); } else { $("#DCC").prop('checked', false); }
}

//Sự kiện thay đổi checkbox DCC
function Change_checkbox_DCC(element) {
    if ($(element).is(":checked")) { $("#CodeRole").val('R-00022') } else { $("#CodeRole").val(''); }
}


//Thêm USER MỚI hiện modal
function SHOW_ADD_USER() {
    thaothac = 'Create';
    RESET_AREA('Div_userinf');
    $("#div_btnUpdate").prop('hidden', true);
    $("#div_btnCreate").removeAttr('hidden');
    $("#Div_pass1").removeAttr('hidden');
    $("#Div_pass2").removeAttr('hidden');
    $("#Div_None").removeAttr('hidden');
    $("#modaledituser").modal('show');
}


//DELETE_USER(this) Xóa tài khoản
function DELETE_USER(element) {
    function func(element) {
        var id = $(element).attr('id');
        id = id.substring(id.indexOf('_') + 1);
        var data = { TenDangNhap: id };
        data.Action = 'DELETE';
        $.ajax({
            type: 'GET',
            url: '/Action_Acount/',
            data: data,
            success: function(response) { Alert_OK(); },
            error: function(response) { AlertErrorSQL(response); }
        });
    }
    CONFIRM_ALERT_Param("您是否操作？Bạn có chắc chắn muốn thực hiện？", "帳號會被刪除 / Tài khoản sẽ bị xóa khỏi hệ thống", '同意 / Đồng ý', '拒絕 / Từ chối', func, element);
}


//Khôi  phục pasword về mặc định
function ResetPassword(element) {
    function RESET_PASS_ACOUNT(element) {
        var id = $(element).attr('id');
        id = id.substring(id.lastIndexOf('_') + 1);
        var data = { TenDangNhap: id };
        data.Action = 'RESET';
        $.ajax({
            type: 'GET',
            url: '/Action_Acount/',
            data: data,
            success: function(response) {
                Alert_OK();
            },
            error: function(response) { AlertErrorSQL(response); }
        });
    }
    CONFIRM_ALERT_Param('您想重設密碼嗎<br/>Bạn muốn reset mật khẩu？', "新密碼 / Mật khẩu mới là: foxconn168!!", "同意 / Đồng ý", '拒絕 / Từ chối', RESET_PASS_ACOUNT, element);
}



//Thêm sửa xóa tài khoản
function ACTION_USER(Action) {
    var data = GET_ALL_INPUT_FROM_DIV('Base_info');
    data.Action = Action;
    var Department = GET_CHECKED_CHECKBOX_FROM_DIV('group_Dept');
    var Poisition = GET_CHECKED_CHECKBOX_FROM_DIV('group_permiss');
    var Manager_Room = ''
    $("#select_manager span").each(function() {
        Manager_Room = Manager_Room + $(this).text() + ",";
    });

    var title = "通報 / Thông báo";
    var btn_OK = "同意 / Đồng ý";
    var btn_Cancel = "拒絕 / Từ chối";
    var title_warning = "您是否操作？<br/> Bạn có chắc chắn muốn thực hiện?";


    data.Department = Department;
    data.Poisition = Poisition;
    data.Manager_Room = Manager_Room;
    if ($('#DCC').is(":checked")) {
        data['DCC'] = '1';
    } else { data['DCC'] = '0'; }


    if (Action == 'CREATE') {
        if ($("#TenDangNhap").val() == '') { Show_Alert(title, btn_OK, "賬款不能為空 / Tên đăng nhập không được phép bỏ trống!"); return; }
        if ($("#HoTen").val() == '') { Show_Alert(title, btn_OK, "姓名不能為空 / Họ tên không được phép bỏ trống!"); return; }
        if ($("#Email").val() == '') { Show_Alert(title, btn_OK, "郵箱不能為空 / Email không được phép bỏ trống!"); return; }
        if ($("#SoDienThoai").val() == '') { Show_Alert(title, btn_OK, "電話號碼不能留空 / Số điện thoại không được phép bỏ trống!"); return; }
        if ($("#CodeRole").val() == '') { Show_Alert(title, btn_OK, "選擇不允許的權限留空 / Chọn quyền hạn không được phép bỏ trống!"); return; }
        if ($("#pass1id").val() == '' || $("#pass2id").val() == '') { Show_Alert(title, btn_OK, "密碼不能為空 / Mật khẩu không được phép bỏ trống!"); return; }
        if ($("#pass1id").val() != $("#pass2id").val()) { Show_Alert(title, btn_OK, "缺乏信息 Mật khẩu không khớp nhau!"); return; }
        if ($("#pass1id").val().length < 8) { Show_Alert(title, btn_OK, "密碼太短 / Mật khẩu quá ngắn(độ dài >=8)!"); return; }
        if (Object.keys(Department).length < 1) { Show_Alert(title, btn_OK, "部門沒有信息 / Phòng ban chưa có thông tin!"); return; }
        // if (Object.keys(Poisition).length < 1) { Show_Alert(title, btn_OK, "職位暫無信息 / Chức vụ chưa có thông tin!"); return; }
        func();
    } else if (Action == 'UPDATE') {
        func();
    } else if (Action == 'DELETE') { CONFIRM_ALERT(title_warning, "帳號會被刪除 / Tài khoản sẽ bị xóa khỏi hệ thống", btn_OK, btn_Cancel, func); }

    function func() {
        AJAX_REQUEST('/Action_Acount/', 'GET', data, Alert_OK);
        $("#modaledituser").modal('hide');
    }
}


//Ẩn hiện mật khẩu Show and Hide password
function SHOW_PASSWORD(element) {

    var x = document.getElementById("pass1id");
    var y = document.getElementById("pass2id");
    if (x.type === "password") {
        x.type = "text";
        y.type = "text";
        element.className = "fad fa-eye";
    } else {
        x.type = "password";
        y.type = "password";
        element.className = "fad fa-eye-slash";
    }
}



//Các sự kiện chờ trong DOCUMENT (event)
$(document).ready(function() {

    // Sự kiện enter input text
    $("#ValueFind").keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {
            Search_User();
        }
    });

    //Chọn ROW giữ trạng thái chọn trong bảng
    $('#table_Viewuser').on('click', '.clickable-row', function(event) {
        $(this).addClass('table-warning').siblings().removeClass('table-warning');

    });

});