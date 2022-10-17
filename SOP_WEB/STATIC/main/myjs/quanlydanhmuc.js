// #CT-00002:Phòng ban
// #CT-00001:Chức vụ
// #CT-00003:Nhà xưởng
// #CT-00010:Loại văn bản
// #CT-00005:Trạng thái thẩm duyệt
// #CT-00006:Nhóm menu
// #CT-00007:Kết án
// #CT-00008:Cài đặt Email
// #CT-00009:Thời gian lưu trữ
// #CT-00010:Loại văn kiện
//Load các loại danh mục
function load_OptionCategorys(CatTypeCode) {
    var num = 0;
    $("#body_OptionCategorys").empty();
    $("#CatTypeCode").val(CatTypeCode);
    //Lấy danh sách các danh mục  
    function func(response) {

        response['returndata'].forEach(function FILL_DATA(item, index) {
            //$("#CatTypeCode").val(item['CatTypeCode']);
            num += 1;
            $("#body_OptionCategorys").append(
                '<tr>\
                    <td>' + num + '</td>\
                    <td id="CatCode_' + item['CatCode'] + '">' + item['CatCode'] + '</td>\
                    <td id="CatName_' + item['CatCode'] + '">' + item['CatName'] + '</td>\
                    <td id="Code_' + item['CatCode'] + '">' + (item['Code'] ? item['Code'] : '') + '</td>\
                    <td class="text-center">\
                    <i id="btnEditDept_' + item['CatCode'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="Edit_Categorys(this.id)"></i>\
                    <i class="fas ">&nbsp;||&nbsp;</i>\
                    <i id="btnDelDept_' + item['CatCode'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="Action_Categorys(' + "'DELETE'" + ',this)"></i>\
                    </td>\
                </tr>');
        });
    }

    //Lấy danh sách các menu
    function func_loadMenu(response) {
        $("#Groups").empty();
        response['returndata'].forEach(function FILL_DATA(item, index) {
            $("#Groups").val(item['Groups']);
            num += 1;
            $("#body_OptionCategorys").append(
                '<tr>\
                    <td>' + num + '</td>\
                    <td id="Code_' + item['Code'] + '">' + item['Code'] + '</td>\
                    <td id="Name_' + item['Code'] + '">' + item['Name'] + '</td>\
                    <td id="Groups_' + item['Code'] + '" name="' + item['Groups'] + '">' + (item['Groups1'] ? item['Groups1'] : '') + '</td>\
                    <td class="text-center">\
                        <i id="btnEditMenu_' + item['Code'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="Edit_Menus(this.id)"></i>\
                        <i class="fas ">&nbsp;||&nbsp;</i>\
                        <i id="btnDelMenu_' + item['Code'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="Action_Menus(' + "'DELETE'" + ',this)"></i>\
                    </td>\
                </tr>');
        });

        //Lấy danh sách nhóm menu
        // $("#Groups").append('<option value="" data-i18n=""></option>');
        response['returndata1'].forEach(function FILL_DATA(item, index) {
            $("#Groups").append('<option value="' + item['CatCode'] + '" data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</option>');
        });
    }


    //Lấy danh danh sách menu đã xóa
    function func_loadDeledtedMenu(response) {
        $("#Groups").empty();
        response['returndata'].forEach(function FILL_DATA(item, index) {
            num += 1;
            $("#body_OptionCategorys").append(
                '<tr>\
                        <td>' + num + '</td>\
                        <td id="Code_' + item['Code'] + '">' + item['Code'] + '</td>\
                        <td id="Name_' + item['Code'] + '">' + item['Name'] + '</td>\
                        <td id="Groups_' + item['Code'] + '" name="' + item['Groups'] + '">' + (item['Groups1'] ? item['Groups1'] : '') + '</td>\
                        <td class="text-center">\
                            <i id="btnRestoreMenu_' + item['Code'] + '" class="fas fa-sync-alt fa-spin f-18 text-danger"  title="Restore Menu" style="cursor: pointer;" onclick="Action_Menus(' + "'RESTORE'" + ',this)"></i>\
                        </td>\
                    </tr>');
        });

        //Lấy danh sách nhóm menu
        // $("#Groups").append('<option value="" data-i18n=""></option>');
        response['returndata1'].forEach(function FILL_DATA(item, index) {
            $("#Groups").append('<option value="' + item['CatCode'] + '" data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</option>');
        });
    }


    if (CatTypeCode == 'MN') {
        AJAX_REQUEST_RESPONSE('/get_OptionCategorys/', 'GET', { CatTypeCode: CatTypeCode }, func_loadMenu);
        $("#btn_AddCategory")
            .removeAttr('onclick')
            .attr('onclick', "Show_Modal_AddMenu()");
    } else if (CatTypeCode == 'LIST-DEL-MENUS') {
        AJAX_REQUEST_RESPONSE('/get_OptionCategorys/', 'GET', { CatTypeCode: CatTypeCode }, func_loadDeledtedMenu);
        $("#btn_AddCategory")
            .removeAttr('onclick')
            .attr('onclick', "Show_Modal_AddMenu()");
    } else {
        AJAX_REQUEST_RESPONSE('/get_OptionCategorys/', 'GET', { CatTypeCode: CatTypeCode }, func);
        $("#btn_AddCategory")
            .removeAttr('onclick')
            .attr('onclick', "Show_Modal_AddCategorys()");
    }

}



//Hiển thị categorys
function Show_Modal_AddCategorys() {
    if ($("#CatTypeCode").val() == '') { Show_Alert("通知 / Thông báo", "同意 Đồng ý", "您尚未選擇類別 / Bạn chưa chọn danh mục"); return; }
    $("#CatCode").val('');
    $("#CatName").val('');
    $("#Code").val('');
    $("#div_btnCreate").removeAttr('hidden');
    $("#div_btnUpdate").prop('hidden', true);
    $("#modal_edit_menu").modal('show');
}


//Hiển thị Menus
function Show_Modal_AddMenu() {
    RESET_AREA('Div_areadMenu');
    $("#div_btnCreate1").removeAttr('hidden');
    $("#div_btnUpdate1").prop('hidden', true);
    $("#modal_edit_menus").modal('show');
}



//Chỉnh sửa 1 Categorys
function Edit_Categorys(ID_element) {
    $("#div_btnCreate").prop('hidden', true);
    $("#div_btnUpdate").removeAttr('hidden');
    var id = ID_element.substring(ID_element.lastIndexOf("_") + 1);
    $("#CatCode").val($("#CatCode_" + id).text());
    $("#CatName").val($("#CatName_" + id).text());
    $("#Code").val($("#Code_" + id).text());
    $("#modal_edit_menu").modal('show');
}




//Chỉnh sửa 1 Menus
function Edit_Menus(ID_element) {
    RESET_AREA('Div_areadMenu');
    $("#div_btnCreate1").prop('hidden', true);
    $("#div_btnUpdate1").removeAttr('hidden');
    var id = ID_element.substring(ID_element.lastIndexOf("_") + 1);
    // alert($("#Code_" + id).text());
    $("#Groups").val($("#Groups_" + id).attr('name'));
    $("#Name").val($("#Name_" + id).text());
    $("#Code1").val($("#Code_" + id).text());
    $("#modal_edit_menus").modal('show');
}





//Thao tác thêm sửa xóa Categorys
function Action_Categorys(Action, element) {
    var data = GET_ALL_INPUT_FROM_DIV('Div_areadCategorys');
    data.Action = Action;
    if (Action == 'CREATE' || Action == 'UPDATE') {
        if ($("#CatTypeCode").val() == '') { Show_Alert("通知 / Thông báo", "同意 Đồng ý", "您尚未選擇類別 / Bạn chưa chọn danh mục"); return; }
        if ($("#CatName").val() == '') { Show_Alert("通知 / Thông báo", "同意 Đồng ý", "您缺少組名信息 / Bạn đang thiếu thông tin tên nhóm"); return; }
        AJAX_REQUEST('/action_Categorys/', 'GET', data, Auto_Click_MenuCategorys);
    } else if (Action == 'DELETE') {
        var CatCode = $(element).attr('id');
        CatCode = CatCode.substring(CatCode.lastIndexOf("_") + 1);
        data.CatCode = CatCode;
        data.CatTypeCode = $('#CatTypeCode').val();

        function func() {
            AJAX_REQUEST('/action_Categorys/', 'GET', data, Auto_Click_MenuCategorys);
        }
        Remind_Question(func);
    }

    $("#modal_edit_menu").modal('hide');
}



//Thao tác thêm sửa xóa Menus
function Action_Menus(Action, element) {
    var data = {
        Code: $("#Code1").val(),
        Name: $("#Name").val(),
        Groups: $("#Groups").val()
    };
    data.Action = Action;

    function func() {
        AJAX_REQUEST('/action_Menus/', 'GET', data, Auto_Click_MenuCategorys);
    }


    if (Action == 'CREATE' || Action == 'UPDATE') {
        if ($("#Groups").val() == '') { Show_Alert("通知 / Thông báo", "同意 Đồng ý", "您尚未選 小組  / Chưa chọn nhóm menu"); return; }
        if ($("#Name").val() == '') { Show_Alert("通知 / Thông báo", "同意 Đồng ý", "您缺少 名稱 / Bạn đang thiếu tên menu"); return; }
        AJAX_REQUEST('/action_Menus/', 'GET', data, Auto_Click_MenuCategorys);
    } else if (Action == 'DELETE' || Action == 'RESTORE') {
        var Code = $(element).attr('id');
        Code = Code.substring(Code.lastIndexOf("_") + 1);
        data.Code = Code;
        data.Groups = $('#Groups_' + Code).attr('name');
        Remind_Question(func);
    }

    $("#modal_edit_menus").modal('hide');
}




//Chuyển trạng thái màu sắc khi nhấn menu quyền hạn
function Set_Effect_Menu(element) {
    $('#navbarToggleExternalContent>ul li').removeAttr('style');
    $(element).prop('style', 'background-color:#343a40 !important;color:white !important;')
}


//Tự động click lại menu danh mục
function Auto_Click_MenuCategorys() {
    $("#navbarToggleExternalContent>ul li").each(function() {
        if ($(this)[0].hasAttribute("style")) {
            $(this).click();
        }
    });

}




//Ẩn hiện bảng quản lý danh mục
function Hide_Show_table(id_table_hide, id_table_show) {
    $('#' + id_table_hide).attr('hidden', '');
    $('#' + id_table_show).removeAttr('hidden');
}




//Hiển thị Modal add Dept công văn đến
function Show_Modal_Dept(Action, element) {

    RESET_AREA('Div_areadDept');
    if (Action == 'INSERT') {
        $("#btn_updateDept").attr('onclick', "Action_DeptArrive('INSERT',$('#" + element.id + "'))");
    } else if (Action == 'UPDATE' || Action == 'DELETE') {
        $("#btn_updateDept").attr('onclick', "Action_DeptArrive('UPDATE',$('#" + element.id + "'))");
        var value = $(element).attr('value');
        $("#Department").val(value);
        $("#UserName").val($("#UserName_" + value).attr('value'));
        $("#Manager").val($("#Manager_" + value).attr('value'));
    }
    if (Action == 'DELETE') {
        Remind_Question_Option(Action_DeptArrive, Action);
        return;
    }
    $("#modal_edit_Dept").modal('show');
}


//Thao tác với bảng quản lý phòng ban
function Action_DeptArrive(Action, element) {
    var data = GET_ALL_INPUT_FROM_DIV('Div_areadDept');
    data.Action = Action
    if (Action == 'DELETE') {
        AJAX_REQUEST_RESPONSE('/action_DeptArr/', 'GET', data, func);
    } else if (Action == 'INSERT' || Action == 'UPDATE' || Action == 'SELECT') {
        AJAX_REQUEST_RESPONSE('/action_DeptArr/', 'GET', data, func);
    }

    function func(response) {
        RESET_AREA('Div_areadDept');
        $("#modal_edit_Dept").modal('hide');

        if (Action != 'SELECT') { Alert_OK() }
        $("#body_OptionDept").empty();
        var num = 0;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            num += 1;
            $("#body_OptionDept").append('<tr>\
                    <td>' + num + '</td>\
                    <td id="Department_' + item['Department'] + '" value="' + item['Department'] + '">' + item['Department1'] + '</td>\
                    <td id="UserName_' + item['Department'] + '" value="' + item['UserName'] + '">' + item['UserName'] + '</td>\
                    <td id="Manager_' + item['Department'] + '" value="' + item['Manager'] + '">' + item['Manager'] + '</td>\
                    <td class="text-center">\
                        <i id="btnEditMenu_' + item['Department'] + '" value="' + item['Department'] + '" class="fas fa-edit text-info" style="cursor: pointer;" onclick="Show_Modal_Dept(' + "'UPDATE'" + ',this)"></i>\
                        <i class="fas ">&nbsp;||&nbsp;</i>\
                        <i id="btnDelMenu_' + item['Department'] + '" value="' + item['Department'] + '" class="fas fa-trash-alt text-danger" style="cursor: pointer;" onclick="Show_Modal_Dept(' + "'DELETE'" + ',this)"></i>\
                    </td>\
                </tr>');
        });

    }
}


//Load modal tổng giám đốc
function Show_Modal_TongGiamDoc() {
    function func(response) {
        response['returndata'].forEach(function FILL_DATA(item, index) {
            $("#TongGiamDoc").empty()
                .val(item['TongGiamDoc']);
            $("#TenTongGiamDoc").empty()
                .val(item['HoTen']);

            $("#HoTroGiamDoc").empty()
                .val(item['HoTroGiamDoc']);
            $("#TenHoTroGiamDoc").empty()
                .val(item['HoTen1']);
        });
        $("#modal_tgd").modal('show');
    }
    AJAX_REQUEST_RESPONSE('/Action_TGD/', 'GET', { Action: "SELECT" }, func)

}

//Lưu tổng giám đốc
function Save_TGD() {
    function func() {
        Alert_OK();
        $("#modal_tgd").modal('hide');
    }
    var data = GET_ALL_INPUT_FROM_DIV('Div_areadTGD');
    data.Action = 'UPDATE';
    AJAX_REQUEST('/Action_TGD/', 'GET', data, func);
}