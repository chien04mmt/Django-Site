var userx = '';


//Lấy danh sách các nhóm quyền hạn vào model cấp quyền
function LOAD_LIST_PERMISSION() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_areaPermiss');
    data.Action = "SELECT";
    AJAX_REQUEST_RESPONSE('/action_groups_permiss/', 'GET', data, func);

    function func(response) {
        $("#Code_Permission").empty().append('<option selected="selected" value="" data-i18n="chonnhom">---Chọn nhóm---</option>');
        response['returndata'].forEach(function(item, index) {
            $("#Code_Permission").append('<option value="' + item['Code_Permission'] + '">' + item['Name_Permission'] + '</option>');
        });
    }
}



//Lưu thông tin cấp quyền
function SAVE_PERMISSION() {
    if ($("#Code_Permission").val() == '') { return; }
    var data = GET_ALL_INPUT_FROM_DIV('Div_areaPermiss');
    AJAX_REQUEST('/save_permiss/', 'GET', data, func);

    function func() {
        Alert_OK();
        $("#modal_Permiss").modal('hide');
    }
}



//Hiển thị modal phân quyền
function LOAD_PERMISSION_ACOUNT(element) {
    RESET_AREA('Div_areaPermiss');
    var data = { UserID: $(element).attr('user'), Action: "SELECT" }
    AJAX_REQUEST_RESPONSE('/getInfo_permiss/', 'GET', data, func);

    function func(response) {
        response['returndata'].forEach(function(item, index) {
            $("#Code_Permission").val(item['Code_Permission']);
            $("#UserID").val(item['UserID']);
            $("#UserName").val(item['UserName']);
        });
        $("#modal_Permiss").modal('show');
    }
}



//Tìm kiếm tài khoản
function TIM_TAIKHOAN() {
    var data = { UserID: $("#mathenhanvien").val() }
    AJAX_REQUEST_RESPONSE('/search_acount/', 'GET', data, func);

    function func(response) {
        $("#table_acount").DataTable().destroy();
        $("#tbody_acount").empty();
        var no = 1;
        response['returndata'].forEach(function FILL_DATA(item, value) {
            $("#tbody_acount").append(
                '\
                <tr class="clickable-row">\
                    <td>' + no + '</td>\
                    <td style="color:Blue;text-decoration:underline;cursor:pointer" onclick="Show_Acount_info(this);" id="UserID_' + item['ID'] + '" user="' + item['UserID'] + '">' + item['UserID'] + '</td>\
                    <td>' + item['DFSite'] + '</td>\
                    <td>' + item['Dept'] + '</td>\
                    <td>' + item['UserName'] + '</td>\
                    <td>' + item['CostNo'] + '</td>\
                    <td>' + item['Telephone'] + '</td>\
                    <td>' + item['mailbox'] + '</td>\
                    <td class="text-center">\
                        <i class="fas fa-edit " id="btnpermiss_' + item['ID'] + '" user="' + item['UserID'] + '" style="cursor: pointer;" onclick="LOAD_PERMISSION_ACOUNT(this);"></i><i class="fas ">\
                    </td>\
                    <td class="text-center">\
                        <i id="btnEdit_' + item['ID'] + '" user="' + item['UserID'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="Show_Acount_info(this)"></i><i class="fas ">&nbsp;||&nbsp;</i>\
                        <i id="btnDel_' + item['ID'] + '" user="' + item['UserID'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="delete_flow_setting(this);"></i>\
                    </td>\
                </tr>\
                '
            );
            no += 1;
        })
        $("#table_acount").DataTable();

    }
}

//Ẩn hiện mục password
function HIDE_INPUT_PASS() {
    $("#show_pass2").prop("hidden", true);
    $("#show_pass1").prop("hidden", true);
}
//Ẩn hiện mục password
function SHOW_INPUT_PASS() {
    $("#show_pass2").removeAttr("hidden");
    $("#show_pass1").removeAttr("hidden");
    RESET_MODAL_USER();
}

//Hiển thị modal thông tin tài khoản
function Show_Acount_info(element) {
    data = { UserID: $(element).attr('user') }
    AJAX_REQUEST_RESPONSE('/search_acount/', 'GET', data, func);

    function func(response) {
        var password = response['password'];
        response['returndata'].forEach(function(item, value) {
            $("#id_userx").text(item['UserName']);
            $("#userid_modal_user").val(item['UserID']);
            $("#usernameid_modal_user").val(item['UserName']);
            $("#id_userx").text(item['UserName']);
            $("#empnoid_modal_user").val(item['Emp_NO']);
            $("#deptid_modal_user").val(item['Dept']);
            $("#costnoid_modal_user").val(item['CostNo']);
            $("#extid_modal_user").val(item['Telephone']);
            $("#emailid_modal_user").val(item['mailbox']);
            $("#pass1id").val(password);
            $('#buid').val(item['division']);
            $('#siteid_modal_user').val(item['DFSite']);
            var img = item['img'];

            if (img == null) {
                $("#bg_user img").remove('img');
                $("#bg_user").append('<img src="' + urlstatic_JS + 'img/pen.jpg">');
            } else {
                $("#bg_user img").remove('img');
                $("#bg_user").append('<img src="' + urlstatic_JS + "media/" + img + '">');
            }

        })
        HIDE_INPUT_PASS();
        $("#modaledituser").modal('show');
    }

}





//Lưu lại thông tin chỉnh sửa Edit User trong modal
function SaveModifyProfile_user() {
    var data = {
        userID: $("#userid_modal_user").val().toUpperCase(),
        DFSite: $("#siteid_modal_user").val(),
        division: $("#buid").val(),
        UserName: $("#usernameid_modal_user").val(),
        Emp_NO: $("#empnoid_modal_user").val().toUpperCase(),
        Dept: $("#deptid_modal_user").val(),
        CostNo: $("#costnoid_modal_user").val().toUpperCase(),
        Telephone: $("#extid_modal_user").val(),
        mailbox: $("#emailid_modal_user").val()
    };
    AJAX_REQUEST('/saveprofile_user/', 'GET', data, func);

    function func() {
        Alert_OK();
        $("#modaledituser").modal('hide');
        TIM_TAIKHOAN();
    }
}



//Các sự kiện chờ trong DOCUMENT (event)
$(document).ready(function() {

    // Sự kiện enter input text
    $("#mathenhanvien").keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {
            TIM_TAIKHOAN();
        }
    });


});