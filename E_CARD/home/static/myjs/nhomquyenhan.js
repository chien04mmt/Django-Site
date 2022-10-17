//---------------------------------------------THAO TÁC VỚI BẢNG [ListPermission]--------------------------------------------------
//Lưu cài đặt nhóm quyền hạn
function Save_Group_Permiss() {
    if ($("#CodeRole").val() == '') { return; }
    var data = GET_CHECKED_CHECKBOX_FROM_DIV('tbody_menus');
    data.Action = "INSERT";
    data.ode_Permission = $("#CodeRole").val();
    AJAX_REQUEST('/action_modules/', 'GET', data, Alert_OK);
}



//Hiển thị modal thêm sửa nhóm phân quyền
function Show_Modal_Group_Permiss() {
    RESET_AREA('Div_AreaRole');
    $("#Code_Permission").prop('hidden', true);
    $("#Div_btnUpdate_GroupPermiss").prop('hidden', true);
    $("#Div_btnCreate_GroupPermiss").removeAttr('hidden');
    $("#modal_groupPermiss").modal('show');

}


//Load thông tin của nhóm quyền hạn
function EditRole_(element) {
    RESET_AREA('modal_groupPermiss');
    $("#Code_Permission").val($(element).attr('Code_Permission'));
    $("#Name_Permission").val($(element).attr('Name_Permission'));
    $("#Detail_Permission").val($(element).attr('Detail_Permission'));
    $("#Div_btnUpdate_GroupPermiss").removeAttr('hidden');
    $("#Div_btnCreate_GroupPermiss").prop('hidden', true);
    $("#Code_Permission").removeAttr('hidden');
    $("#modal_groupPermiss").modal('show');

}


//Thêm hoặc sửa,xóa nhóm phân quyền
function ACTION_GROUP_PERMISS(Action, element) {
    var data = GET_ALL_INPUT_FROM_DIV("Div_AreaRole");
    data.Action = Action;

    function func() {
        AJAX_REQUEST_RESPONSE('/action_groups_permiss/', 'GET', data, func1);
    }


    function func1(response) {
        $("#tbody_permiss").empty();
        $("#CodeRole").empty()
            .append('<option selected="selected" value="" data-i18n="chonnhom">---Chọn nhóm---</option>');

        var num = 0;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            num += 1;
            $("#tbody_permiss").append('<tr class="clickable-row">\
                        <td>' + num + '</td>\
                        <td id="tdCodepermiss_' + num + '">' + item['Code_Permission'] + '</td>\
                        <td id="tdNamepermiss_' + num + '">' + item['Name_Permission'] + '</td>\
                        <td id="tdNamepermiss_' + num + '">' + item['Detail_Permission'] + '</td>\
                        <td class="text-center">\
                            <i id="btnEditRole_' + num + '" Code_Permission="' + item['Code_Permission'] + '" Name_Permission="' + item['Name_Permission'] + '" Detail_Permission="' + item['Detail_Permission'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="EditRole_(this);"></i><i class="fas ">&nbsp;||&nbsp;</i>\
                            <i id="btnDelRole_' + num + '" Code_Permission="' + item['Code_Permission'] + '" Name_Permission="' + item['Name_Permission'] + '" Detail_Permission="' + item['Detail_Permission'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="ACTION_GROUP_PERMISS(' + "'DELETE'" + ', this)"></i>\
                        </td>\
                </tr>');
            $("#CodeRole").append('<option value="' + item['Code_Permission'] + '" data-i18n="' + item['Name_Permission'] + '">' + item['Name_Permission'] + '</option>');
        });
        SHOW_LANG_();
        $("#modal_groupPermiss").modal('hide');
        if (Action != "SELECT") { Alert_OK() }
    }

    switch (Action) {
        case "SELECT":
            AJAX_REQUEST_RESPONSE('/action_groups_permiss/', 'GET', data, func1)
            break;
        case "INSERT":
            if ($("#Name_Permission").val() == '') { Show_Alert_Message("Thiếu thông tin tên quyền hạn !"); return; }
            AJAX_REQUEST_RESPONSE('/action_groups_permiss/', 'GET', data, func1);
            break;
        case "UPDATE":
            if ($("#Code_Permission").val() == '' || $("#Name_Permission").val() == '') { Show_Alert_Message("Thiếu thông tin tên quyền hạn !"); return; }
            AJAX_REQUEST_RESPONSE('/action_groups_permiss/', 'GET', data, func1);
            break;
        case "DELETE":
            data.Name_Permission = $(element).attr("Name_Permission");
            data.Code_Permission = $(element).attr("Code_Permission");
            Remind_Question(func);
    }
}



//--------------------------------------THAO TÁC VỚI MENU-------------------------------------------------------------------


//Hiểm thị modal thêm mới menu
function Show_modal_AddMenu() {
    RESET_AREA('modal_Menus');
    $("#div_btnCreate1").removeAttr('hidden');
    $("#div_btnUpdate1").prop('hidden', true);
    $("#modal_Menus").modal('show');
}


//Load model sửa menu
function EditMenu_(element) {
    RESET_AREA('modal_Menus');
    $("#Groups_Menu").val($(element).attr('groups_menu'));
    $("#Code_Menu").append('<option value="' + $(element).attr('code_menu') + '" data-i18n="' + $(element).attr('code_menu') + '">' + $(element).attr('code_menu') + '</option>');
    $("#Name_Menu").val($(element).attr('name_menu'));
    $("#div_btnCreate1").prop('hidden', true);
    $("#div_btnUpdate1").removeAttr('hidden');
    $("#modal_Menus").modal('show');
}


//Thao tác thêm sửa xóa Menus
function Action_Menus(Action, element) {

    var data = GET_ALL_INPUT_FROM_DIV('Div_areadMenu');
    data.Action = Action;
    var url = "/action_Menus/";

    function func() {
        AJAX_REQUEST_RESPONSE(url, 'GET', data, func1);
    }


    function func1(response) {

        $("#tbody_menus").empty();
        if (response['returndata'] == undefined) { return; }
        var num = 0;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            num += 1;
            $("#tbody_menus").append(
                '<tr class="text-center clickable-row" for="checkbox_' + item['Code_Menu'] + '" onclick="Row_Click_Checkbox(this)">\
                        <td class="text-center">' + num + '</td>\
                        <td>' + item['Code_Menu'] + '</td>\
                        <td data-i18n="' + item['Name_Menu'] + '">' + item['Name_Menu'] + '</td>\
                        <td>' + item['Groups_Menu'] + '</td>\
                        <td><input id="checkbox_' + item['Code_Menu'] + '" type="checkbox"  Code_Menu="' + item['Code_Menu'] + '" value="0" class="form-control" onclick="" style="height:20px;"></td>\
                        <td class="text-center">\
                            <i id="btnEditMenu_' + item['Code_Menu'] + '" Code_Menu="' + item['Code_Menu'] + '" Name_Menu="' + item['Name_Menu'] + '" Groups_Menu="' + item['Groups_Menu'] + '"  class="fas fa-edit text-info" style="cursor: pointer;" onclick="EditMenu_(this);"></i><i class="fas ">&nbsp;||&nbsp;</i>\
                            <i id="btnDelMenu_' + item['Code_Menu'] + '" Code_Menu="' + item['Code_Menu'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="Action_Menus(' + "'DELETE'" + ',this);"></i>\
                        </td>\
                </tr>');
        });
        SHOW_LANG_();
        if (Action == "DELETE" || Action == "INSERT" || Action == "UPDATE") { Alert_OK(); }
        $("#modal_Menus").modal('hide');
    }
    //Kiểm tra dữ liệu trước khi thao tác
    function check_data() {
        if ($("#Groups_Menu").val() == '') { Show_Alert_Message("Chưa chọn nhóm Menu"); return false; }
        if ($("#Code_Menu").val() == '') { Show_Alert_Message("Bạn đang thiếu thông tin mã Menu"); return false; }
        if ($("#Name_Menu").val() == '') { Show_Alert_Message("Bạn đang thiếu tên Menu"); return false; }
    }

    //Lựa chọn thêm, sửa, xóa , select
    switch (Action) {
        case "INSERT":
            if (check_data() == false) { return; }
            AJAX_REQUEST_RESPONSE(url, 'GET', data, func1);
            break;
        case "UPDATE":
            if (check_data() == false) { return; }
            AJAX_REQUEST_RESPONSE(url, 'GET', data, func1);
            break;
        case "DELETE":
            var Code_Menu = $(element).attr('code_menu');
            data.Code_Menu = Code_Menu;
            Remind_Question(func);
            break;
        case "SELECT":
            AJAX_REQUEST_RESPONSE(url, 'GET', data, func1)
            break;

    }

}




//--------------------------------------THAO TÁC VỚI MODULES-------------------------------------------------------------------
//Load danh sách các submenu với menu chính
function Load_SubMenu(element) {
    var id = $(element).val();
    $("#Code_Menu").empty()
        .append('<option value="" data-i18n=""></option>');
    $("#" + id + " ul li").each(function() {
        $("#Code_Menu").append('<option value="' + $(this).attr('name') + '" data-i18n="' + $(this).attr('name') + '">' + $(this).attr('name') + '</option>');
    });
    SHOW_LANG_();
}



//Thêm sửa xóa modules
function Action_Modules(Action, element) {

    var data = GET_CHECKED_CHECKBOX_FROM_DIV('tbody_menus');
    data.Action = Action;
    var url = "/action_Modules/";

    if ($(element).val() == '') { return; }
    data.Code_Permission = $(element).val();

    function func(response) {
        RESET_AREA('table_menus');
        response['returndata'].forEach(function(item, index) {
            checkbox = document.getElementById("checkbox_" + item['Code_Menu']);
            checkbox.checked = true;
        });
        if (Action == "DELETE" || Action == "INSERT" || Action == "UPDATE") { Alert_OK(); }
    }
    AJAX_REQUEST_RESPONSE(url, 'GET', data, func);
}




//----------------------------------------------------------------------------------------------------------


//Thực hiện click vào row==> input trong bảng được check
function Row_Click_Checkbox(element) {
    var id = $(element).attr('for');
    checkbox = document.getElementById(id);
    if (checkbox.checked) {
        checkbox.checked = false;
        checkbox.value = "0"
    } else {
        checkbox.checked = true;
        checkbox.value = "1"
    }

}




//--------------------------------------HIỆU ỨNG HOVER MENU-------------------------------------------------------------------

//Chuyển trạng thái màu sắc khi nhấn menu quyền hạn
function Set_Effect_Menu(element) {
    $('.menu-permiss')
        .removeAttr('style')
        .removeClass('show')
        .children('div').removeAttr('style');
    $(element)
        .addClass('show')
        .prop('style', 'border-bottom:2px solid #012258;background-color:whitesmoke;')
        .children('div').prop('style', "color:dodgerblue");
}

$(".menu-permiss").hover(
    function() {
        if ($(this).hasClass('show')) { return false; }
        $(this).click();
    }

);