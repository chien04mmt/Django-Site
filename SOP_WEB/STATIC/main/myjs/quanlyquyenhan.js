//Load danh sách rowle quyền hạn
function Load_Roles() {
    $("#body_roles").empty();
    $("#CodeRole").empty()
        .append('<option selected="selected" value="" data-i18n="chonnhom">---Chọn nhóm---</option>');

    $.ajax({
        type: 'GET',
        url: '/load_roles/',
        data: '',
        success: function(response) {
            var num = 0;
            response['returndata'].forEach(function FILL_DATA(item, index) {
                num += 1;
                $("#body_roles").append('<tr>\
                        <td>' + num + '</td>\
                        <td id="tdCodepermiss_' + num + '">' + item['Code'] + '</td>\
                        <td id="tdNamepermiss_' + num + '">' + item['Name'] + '</td>\
                        <td class="text-center">\
                            <i id="btnEditRole_' + num + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="EditRole_(this);"></i><i class="fas ">&nbsp;&nbsp;</i>\
                            <i id="btnDelRole_' + num + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="ACTION_GROUP_PERMISS(' + "'DELETE'" + ', this)"></i>\
                        </td>\
                </tr>');
                $("#CodeRole").append('<option value="' + item['Code'] + '" data-i18n="' + item['Code'] + '">' + item['Name'] + '</option>');

            });
            SHOW_LANG_();

        },
        error: function(response) { AlertErrorSQL(response); }
    });
}

//Load danh sách menu
function Load_Menus() {
    $("#body_menupermiss").empty();
    $.ajax({
        type: 'GET',
        url: '/load_menus/',
        data: '',
        success: function(response) {
            var num = 0;
            response['returndata'].forEach(function FILL_DATA(item, index) {
                num += 1;
                $("#body_menupermiss").append(
                    '<tr class="text-center">\
                        <td>' + num + '</td>\
                        <td>' + item['Code'] + '</td>\
                        <td data-i18n="' + item['Code'] + '">' + item['Name'] + '</td>\
                        <td>' + item['Groups1'] + '</td>\
                        <td><input id="check_' + item['Code'] + '" type="checkbox" class="form-control" onclick="" style="height:20px;"></td>\
                        <td class="text-center">\
                            <i id="btnEditMenu_' + item['Code'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="EditMenu_' + num + '(this);"></i><i class="fas ">&nbsp;&nbsp;</i>\
                            <i id="btnDelMenu_' + item['Code'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="DeleteMenu_' + num + '(this);"></i>\
                        </td>\
                    </tr>');
            });
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//Load quyền hạn của nhóm quyền hạn
function Load_Group_Permiss(element) {
    RESET_AREA('body_menupermiss');
    $.ajax({
        type: 'GET',
        url: '/load_groups_permiss/',
        data: { CodeRole: $(element).val() },
        success: function(response) {
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#check_" + item['Code']).prop('checked', true);
            });
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//Lưu cài đặt nhóm quyền hạn
function Save_Group_Permiss() {
    if ($("#CodeRole").val() == '') { return; }
    var data = GET_CHECKED_CHECKBOX_FROM_DIV('body_menupermiss');
    data.CodeRole = $("#CodeRole").val();

    $.ajax({
        type: 'GET',
        url: '/save_groups_permiss/',
        data: data,
        success: function(response) { Alert_OK(); },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Hiển thị modal thêm sửa nhóm phân quyền
function Show_Modal_Group_Permiss() {
    RESET_AREA('Div_AreaRole');
    var data = {
        NameCol: "Code",
        NameTable: "Roles"
    }
    $.ajax({
        type: 'GET',
        url: '/get_autocode/',
        data: data,
        success: function(response) {
            $("#Code_roles").val(response['Autocode']);
            $("#Div_btnCreate_GroupPermiss").removeAttr('hidden');
            $("#Div_btnUpdate_GroupPermiss").prop('hidden', true);
            $("#modal_groupPermiss").modal('show');
        },
        error: function(response) { AlertErrorSQL(response); }
    });

}


//Load thông tin của nhóm quyền hạn
function EditRole_(element) {
    var id = $(element).attr('id');
    id = id.substring(id.lastIndexOf("_") + 1);
    $("#Code_roles").val($("#tdCodepermiss_" + id).text());
    $("#Name_roles").val($("#tdNamepermiss_" + id).text());
    $("#Div_btnUpdate_GroupPermiss").removeAttr('hidden');
    $("#Div_btnCreate_GroupPermiss").prop('hidden', true);
    $("#modal_groupPermiss").modal('show');
}


//Thêm hoặc sửa nhóm phân quyền
function ACTION_GROUP_PERMISS(Action, element) {
    var data = {};
    if (Action != 'DELETE') {
        data = {
            Code: $("#Code_roles").val(),
            Name: $("#Name_roles").val(),
            Action: Action
        };
        func(data);
    } else {
        var id = $(element).attr('id');
        id = id.substring(id.lastIndexOf("_") + 1);
        data = {
            Code: $("#tdCodepermiss_" + id).text(),
            Name: $("#tdNamepermiss_" + id).text(),
            Action: 'DELETE'
        };
        CONFIRM_ALERT_Param("您是否操作？<br/>Bạn có muốn thực hiện？", "小組會被刪除 / Nhóm này sẽ bị xóa khỏi hệ thống.", "同意 / Đồng ý", "拒絕 / Từ chối", func, data);
    }

    function func(data) {
        $.ajax({
            type: 'GET',
            url: '/action_groups_permiss/',
            data: data,
            success: function(response) {
                Alert_OK();
                $("#modal_groupPermiss").modal('hide');
                Load_Roles();
            },
            error: function(response) { AlertErrorSQL(response); }
        });
    }

}





//---------------------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------





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