//------------------------------------------QUẢN LÝ PHÒNG MÁY CHỦ-------------------------------------------------

//Tìm kiếm thông tin
function TRA_CUU_QUYEN_PHONG_MAY() {
    $("#table_data").DataTable().destroy();
    $("#tbody_data").empty();

    function func(response) {
        var num = 1;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            $("#tbody_data").append('<tr>\
                <td>' + num + '</td>\
                <td>' + (item['emp_no'] == null ? "" : item['emp_no']) + '</td>\
                <td>' + (item['cname'] == null ? "" : item['cname']) + '</td>\
                <td>' + (item['yname'] == null ? "" : item['yname']) + '</td>\
                <td>' + (item['deptname'] == null ? "" : item['deptname']) + '</td>\
                <td>' + (item['FACTORYCODE'] == null ? "" : item['FACTORYCODE']) + '</td>\
                <td>' + (item['FREMARK'] == null ? "" : item['FREMARK']) + '</td>\
                <td>' + (item['FBDATE'] == null ? "" : GET_STRING_DATETIME2(item['FBDATE'])) + '</td>\
                <td>' + (item['CreatedBy'] == null ? "" : item['CreatedBy']) + '</td>\
            </tr>');
            num += 1;
        });
        $("#table_data").DataTable();
        RESET_AREA('Div_modal');
        $("#modal_optionSearch").modal('hide');
    }
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    //console.log($("#START_TIME").val());
    data.START_TIME = ReplaceAll($("#START_TIME").val(), '/', '-');
    data.END_TIME = ReplaceAll($("#END_TIME").val(), '/', '-');
    data.CreatedBy = $("#CreatedBy").val();
    AJAX_REQUEST_RESPONSE('/tracuuquyenphongmay/', 'GET', data, func);
}


//Tìm kiếm thông tin trong bảng lịch sử thao tác
function TRA_CUU_LICHSU() {
    $("#table_data").DataTable().destroy();
    $("#tbody_data").empty();
    var num = 1;

    function func(response) {
        response['returndata'].forEach(function FILL_DATA(item, index) {
            var action = item['action'];
            if (action === "INSERT") { action = '<i class="fas fa-user-plus text-success f-20"></i>' } else { action = '<i class="fas fa-user-slash text-danger f-20"></i>' }
            $("#tbody_data").append('<tr>\
                <td>' + num + '</td>\
                <td>' + item['emp_no'] + '</td>\
                <td>' + item['cname'] + '</td>\
                <td>' + item['yname'] + '</td>\
                <td>' + item['deptname'] + '</td>\
                <td>' + item['FACTORYCODE'] + '</td>\
                <td>' + item['logip'] + '</td>\
                <td>' + action + '</td>\
                <td>' + GET_STRING_DATETIME2(item['CreatedDate']) + '</td>\
                <td>' + ReplaceAll(item['CreatedBy'], ' ', '') + '</td>\
            </tr>');
            num += 1;
        });
        $("#table_data").DataTable()
    }
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    AJAX_REQUEST_RESPONSE('/tracuulichsu/', 'GET', data, func);
}


//Xóa một mã thẻ khỏi cơ sở dũ liệu
function DELETE_PERSON() {
    if ($("#emp_no").val() == '') { Show_Alert_Message('Nhập vào thông tin trường mã nhân viên!'); return; }
    //if ($("#deptname").val() == '') { Show_Alert_Message('Thiếu thông tin phòng ban !'); return; }
    //if ($("#FACTORYCODE").val() == '') { Show_Alert_Message('Thiếu thông tin nhà máy !'); return; }

    function func() {
        var data = GET_ALL_INPUT_FROM_DIV('Div_area');
        AJAX_REQUEST_RESPONSE('/delete_person/', 'GET', data, TRA_CUU_QUYEN_PHONG_MAY);
    }
    Remind_Question(func);
}


//Thêm một mã thẻ vào cơ sở dũ liệu
function ADD_PERSON() {
    if ($("#emp_no").val() == '') { Show_Alert_Message('Thiếu thông tin mã thẻ !'); return; }
    if ($("#cname").val() == '') { Show_Alert_Message('Thiếu tên tiếng Trung !'); return; }
    if ($("#yname").val() == '') { Show_Alert_Message('Thiếu tên tiếng Việt !'); return; }
    if ($("#deptname").val() == '') { Show_Alert_Message('Thiếu thông tin phòng ban !'); return; }
    if ($("#FACTORYCODE").val() == '') { Show_Alert_Message('Thiếu thông tin nhà máy !'); return; }
    if ($("#FREMARK").val() == '') { Show_Alert_Message('Hãy nhập lý do thêm vào mục ghi chú !'); return; }

    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    AJAX_REQUEST_RESPONSE('/add_person/', 'GET', data, TRA_CUU_QUYEN_PHONG_MAY);
}


//Đăng file danh sách exel lên server
function UPLOAD_EXEL_LIST(Action) {
    function func(response) {
        $("#table_data").DataTable().destroy();
        $("#tbody_data").empty();

        var num = 1;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            $("#tbody_data").append('<tr>\
                <td>' + num + '</td>\
                <td>' + (item['emp_no'] == null ? "" : item['emp_no']) + '</td>\
                <td>' + (item['cname'] == null ? "" : item['cname']) + '</td>\
                <td>' + (item['yname'] == null ? "" : item['yname']) + '</td>\
                <td>' + (item['deptname'] == null ? "" : item['deptname']) + '</td>\
                <td>' + (item['FACTORYCODE'] == null ? "" : item['FACTORYCODE']) + '</td>\
                <td>' + (item['FREMARK'] == null ? "" : item['FREMARK']) + '</td>\
                <td>' + (item['FBDATE'] == null ? "" : GET_STRING_DATETIME2(item['FBDATE'])) + '</td>\
                <td>' + (item['CreatedBy'] == null ? "" : item['CreatedBy']) + '</td>\
            </tr>');
            num += 1;
        });
        $("#table_data").DataTable();
    }

    // Sử dụng jquery:
    var formData = GET_FORM_DATA_TO_POST('File_upload');
    formData.append('Action', Action);
    AJAX_POST_REQUEST_RESPONSE('/uploadexel/', formData, func)
}


//tra cứu nhật ký ra vào phòng máy chủ
function GET_LOG_SERVERROOM() {
    $("#table_data").DataTable().destroy();
    $("#tbody_data").empty();
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    AJAX_REQUEST_RESPONSE('/log_In_Out_SVR/', 'GET', data, func);

    function func(response) {
        var num = 1;
        response['returndata'].forEach(function(item, index) {
            var STATUS = item['STATUS'];
            if (STATUS.includes('RED')) { STATUS = '<i class="fad fa-credit-card text-danger f-24"></i>' } else { STATUS = '<i class="fad fa-credit-card text-success f-24"></i>' }

            $("#tbody_data").append('<tr>\
                <td>' + num + '</td>\
                <td>' + item['CARD_NO'] + '</td>\
                <td>' + item['EMP_NO'] + '</td>\
                <td>' + item['EMP_NAME'] + '</td>\
                <td>' + item['GRP'] + '</td>\
                <td>' + item['TYPES'] + '</td>\
                <td>' + item['DEPT'] + '</td>\
                <td>' + GET_STRING_DATETIME2(item['INTIME']) + '</td>\
                <td>' + item['MAC'] + '</td>\
                <td>' + item['POS'] + '</td>\
                <td>' + item['IP'] + '</td>\
                <td>' + STATUS + '</td>\
            </tr>');
            num += 1;
        });
        $("#table_data").DataTable();
    }
}



//#Xuất file exel quyền ra vào phòng máy chủ
function PRINT_EXEL_PERMISS_SERVER() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    data.START_TIME = ReplaceAll($("#START_TIME").val(), '/', '-');
    data.END_TIME = ReplaceAll($("#END_TIME").val(), '/', '-');
    data.CreatedBy = $("#CreatedBy").val();
    AJAX_REQUEST_RESPONSE('/print_exel_permiss_server/', 'GET', data, func);

    function func(response) {
        window.open(response['returndata'], '_blank')
    }
}


//#Xuất file exel log vào ra phòng máy
function PRINT_EXEL_LOG_INOUT_SERVER() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    AJAX_REQUEST_RESPONSE('/print_exel_inout_server/', 'GET', data, func);

    function func(response) {
        window.open(response['returndata'], '_blank')
    }
}


//#Xuất file exel log thao tác phòng máy
function PRINT_EXEL_LOG_ACTION_SERVER() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    AJAX_REQUEST_RESPONSE('/print_exel_action_server/', 'GET', data, func);

    function func(response) {
        window.open(response['returndata'], '_blank')
    }
}



//Thực hiện chọn file 
function FILE_SELECTED(element) {
    var x = document.getElementById(element.id);
    var file = '';
    if ('files' in x) {
        if (x.files.length == 0) {
            $("#btn_addUp,#btn_delUp").attr('hidden', true);
            return false;
        } else {
            for (var i = 0; i < x.files.length; i++) {
                file = x.files[i];
                if ('name' in file) {
                    // Lấy tên file file.name
                }
                if ('size' in file) {
                    //lẤY KÍCH THƯỚC FILE  file.size
                }
            }
        }
    } else {
        if (x.value == "") {
            $("#btn_addUp,#btn_delUp").attr('hidden', true);
            return false;
        } else {
            // If the browser does not support the files property, it will return the path of the selected file instead. 
        }
    }
    $("#btn_addUp,#btn_delUp").removeAttr('hidden', true);
}



$(document).ready(function() {

});