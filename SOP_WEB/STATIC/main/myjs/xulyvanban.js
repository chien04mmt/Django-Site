//--------------------------------//Xem chi tiết đơn xin mã VB :----------------------------------------------
//--------------------------------//Xem chi tiết đơn hủy mã VB :----------------------------------------------
//--------------------------------//Xem chi tiết đơn phát hành VB :-------------------------------------------
//--------------------------------//Xem chi tiết đơn báo phế VB :-------------------------------------------


//Hàm lấy thông tin đơn
function HienthiThongTinDon(url, CodeDocument, id_area) {
    $.ajax({
        type: 'GET',
        url: url,
        data: { 'CodeDocument': CodeDocument },
        success: function(response) {
            RESET_AREA(id_area);
            var obj = ReMove_Null_String(response['returndata']);
            BINDING_DATA_TO_ID(obj)
            Alert_OK();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Chi tiết đơn xin mã văn bản
function ChiTietDon(element) {
    var code = $(element).text();
    var href = 'chitietdon/?CodeDocument=' + code;
    Open_link(href, '_blank');
}

//Đi tới 1 liên kết( host + '/' + href_name ):
function Goto_Document(href_name) {
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/' + href_name
    window.location = newhref;
}

//Lấy thông tin người đăng nhập đưa vào mục người làm đơn
function GET_USER_LOGIN() {
    function func(response) { $("#CreatedBy").val(response['returndata']['HoTen']); }
    AJAX_REQUEST_RESPONSE('/get_userlogin/', 'GET', '', func);
}


//Load danh sách các phòng ban
function load_Department() {
    $.ajax({
        type: 'GET',
        url: '/load_Department/',
        data: 'Department',
        success: function(response) {
            $("#Department").empty()
                .append('<option value="" data-i18n="all">---Tất cả---</option>');

            response['returndata'].forEach(function FILL_DATA(item, index) {
                if (item['Checked'] == '1') {
                    $("#Department").append('<option value="' + item['CatCode'] + '" data-i18n="' + item['CatCode'] + '" selected>' + item['CatName'] + '</option>');
                } else { $("#Department").append('<option value="' + item['CatCode'] + '" data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</option>'); }
            });
            //Alert_OK();
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//--------------------------------//TRA CỨU THÔNG TING :----------------------------------------------
//--------------------------------//TRA CỨU THÔNG TING :----------------------------------------------
//--------------------------------//TRA CỨU THÔNG TING :----------------------------------------------

//Style cho cell trong bang
function Style_cell_Table1(max_width, color, align_text, local_show, title) { return ' style="max-width:' + max_width + ' !important; text-overflow: ellipsis;white-space: nowrap;overflow: hidden;color:' + color + '" class="text-' + align_text + '" data-toggle="tooltip" data-placement="' + local_show + '" title="' + title + '"'; }
//Style cho cell trong bang
function Style_cell_Table(max_width, color, align_text, local_show, title) { return ' text-overflow: ellipsis;white-space: nowrap;overflow: hidden;color:' + color + '" class="text-' + align_text + '" data-toggle="tooltip" data-placement="' + local_show + '" title="' + title + '"'; }


//tra cứu danh sách mã văn bản
function TraCuuTrinhKy() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuutrinhky/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                        <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                        <td ' + Style_cell_Table("130px", "#", "center", "right", item['CodeDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['CodeDocument'] + '" >' + item['CodeDocument'] + '</a></td>\
                        <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocumentNo']) + '>' + item['DocumentNo'] + '</td>\
                        <td ' + Style_cell_Table("100px", "#", "center", "right", item['CreatedBy1']) + '>' + item['CreatedBy1'] + '</td>\
                        <td ' + Style_cell_Table("170px", "#", "center", "right", item['Department']) + ' data-i18n="' + item['Department'] + '">' + item['Department'] + '</td>\
                        <td ' + Style_cell_Table("100px", "#", "center", "right", item['CheckWait']) + '>' + item['CheckWait'] + '</td>\
                        <td ' + Style_cell_Table("150px", "#", "center", "right", item['States']) + ' data-i18n="' + item['States'] + '">' + item['States'] + '</td>\
                        <td ' + Style_cell_Table("130px", "#", "center", "right", item['CreatedDate'].replace('T', ' ')) + '>' + GET_STRING_DATETIME1(item['CreatedDate'].replace('T', ' ')) + '</td>\
                        <td ' + Style_cell_Table("150px", "#", "center", "right", item['Code_Name']) + ' data-i18n="' + item['Code_Name'] + '">' + item['Code_Name'] + '</td>\
                    </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}




//tra cứu danh sách mã văn bản
function TraCuuDSMaVB() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuudsmavb/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                    <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                    <td ' + Style_cell_Table("130px", "#", "center", "right", item['CodeDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['CodeDocument'] + '" >' + item['CodeDocument'] + '</a></td>\
                    <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocNo']) + '>' + item['DocNo'] + '</td>\
                    <td ' + Style_cell_Table("200px", "#", "center", "left", item['DocName']) + '>' + item['DocName'] + '</td>\
                    <td></td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['HoTen']) + '>' + item['HoTen'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['Department_Text']) + ' data-i18n="' + item['Department'] + '">' + item['Department_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['States_Text']) + ' data-i18n="' + item['States'] + '">' + item['States_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['ApplicationDate_Text']) + '>' + item['ApplicationDate_Text'].replace('T', ' ') + '</td>\
                    <td data-i18n="C-00046"></td>\
                    </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//tra cứu danh sách hủy mã văn bản
function TraCuuDSHuyMaVB() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuudshuymavb/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                    <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['CancelDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['CancelDocument'] + '" >' + item['CancelDocument'] + '</a></td>\
                    <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocNo']) + '>' + item['DocNo'] + '</td>\
                    <td ' + Style_cell_Table("200px", "#", "center", "left", item['DocName']) + '>' + item['DocName'] + '</td>\
                    <td></td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['HoTen']) + '>' + item['HoTen'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['Department_Text']) + ' data-i18n="' + item['Department'] + '">' + item['Department_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['States_Text']) + ' data-i18n="' + item['States'] + '">' + item['States_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['ApplicationDate_Text']) + '>' + item['ApplicationDate_Text'].replace('T', ' ') + '</td>\
                    <td data-i18n="C-00050"></td>\
                    </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//tra cứu danh sách phế bỏ văn bản
function TraCuuDSPheBoVB() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuudsphebovb/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                        <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                        <td ' + Style_cell_Table("130px", "#", "center", "right", item['ObsoletedDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['ObsoletedDocument'] + '" >' + item['ObsoletedDocument'] + '</a></td>\
                        <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocumentNo']) + '>' + item['DocumentNo'] + '</td>\
                        <td ' + Style_cell_Table("200px", "#", "left", "right", item['DocumentName']) + '>' + item['DocumentName'] + '</td>\
                        <td ' + Style_cell_Table("90px", "#", "center", "right", item['PublishDocument']) + '>' + item['PublishDocument'] + '</td>\
                        <td ' + Style_cell_Table("90px", "#", "center", "right", item['HoTen']) + '>' + item['HoTen'] + '</td>\
                        <td ' + Style_cell_Table("90px", "#", "center", "right", item['Department_Text']) + ' data-i18n="' + item['Department'] + '">' + item['Department_Text'] + '</td>\
                        <td ' + Style_cell_Table("90px", "#", "center", "right", item['States_Text']) + ' data-i18n="' + item['States'] + '">' + item['States_Text'] + '</td>\
                        <td ' + Style_cell_Table("90px", "#", "center", "right", item['ApplicationDate_Text'].replace('T', ' ')) + '>' + item['ApplicationDate_Text'].replace('T', ' ') + '</td>\
                        <td data-i18n="C-00049"></td>\
                    </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//tra cứu danh sách phát hành văn bản
function TraCuuDSPhatHanhVB() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuudsphathanhvb/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                    <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                    <td ' + Style_cell_Table("130px", "#", "center", "right", item['PublishDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['PublishDocument'] + '" >' + item['PublishDocument'] + '</a></td>\
                    <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocumentNo']) + '>' + item['DocumentNo'] + '</td>\
                    <td ' + Style_cell_Table("200px", "#", "left", "right", item['DocumentName']) + '>' + item['DocumentName'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['Rev']) + '>' + item['Rev'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['HoTen']) + '>' + item['HoTen'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['Department_Text']) + ' data-i18n="' + item['Department'] + '">' + item['Department_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['States_Text']) + ' data-i18n="' + item['States'] + '">' + item['States_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['ApplicationDate_Text'].replace('T', ' ')) + '>' + item['ApplicationDate_Text'].replace('T', ' ') + '</td>\
                    <td data-i18n="C-00047"></td>\
                </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//tra cứu danh sách phát hành văn bản
function TraCuuDSSuaDoiVB() {
    //alert('Chức năng tra cứu trình ký');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/tracuudssuadoivb/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                    <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                    <td ' + Style_cell_Table("130px", "#", "center", "right", item['EditDocument']) + '><a href="javascript:void(0)" onclick="ChiTietDon(this)" style="color:#004aff" id="' + item['EditDocument'] + '" >' + item['EditDocument'] + '</a></td>\
                    <td ' + Style_cell_Table("170px", "#", "center", "right", item['DocumentNo']) + '>' + item['DocumentNo'] + '</td>\
                    <td ' + Style_cell_Table("200px", "#", "left", "right", item['DocumentName']) + '>' + item['DocumentName'] + '</td>\
                    <td>' + item['Rev'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['HoTen']) + '>' + item['HoTen'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['Department_Text']) + ' data-i18n="' + item['Department'] + '">' + item['Department_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['States_Text']) + ' data-i18n="' + item['States'] + '">' + item['States_Text'] + '</td>\
                    <td ' + Style_cell_Table("90px", "#", "center", "right", item['ApplicationDate_Text'].replace('T', ' ')) + '>' + item['ApplicationDate_Text'].replace('T', ' ') + '</td>\
                    <td data-i18n="C-00048"></td>\
                </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//tra cứu phụ lục
function TraCuuCacPhuLuc() {
    //alert('Chức năng tra cứu các phụ lục');
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    $.ajax({
        type: 'GET',
        url: '/timphuluc/',
        data: data,
        success: function(response) {
            Reset_Table_Datatable('table_vanban');
            response['returndata'].forEach(function FILL_DATA(item1, index) {
                var item = ReMove_Null_String(item1);
                $("#tbody_vanban")
                    .append('<tr>\
                    <td class="text-center"><i class="fal fa-file-word f-18 text-info" aria-hidden="true"></i></td>\
                        <td ' + Style_cell_Table("150px", "#", "center", "right", item['FormNo']) + '>' + item['FormNo'] + '</td>\
                        <td ' + Style_cell_Table("170px", "#", "center", "right", item['FormName']) + '>' + item['FormName'] + '</td>\
                        <td ' + Style_cell_Table("150px", "#", "center", "right", item['DocumentNo']) + '>' + item['DocumentNo'] + '</td>\
                        <td ' + Style_cell_Table("100px", "#", "center", "right", item['DocumentName']) + '>' + item['DocumentName'] + '</td>\
                        <td ' + Style_cell_Table("500px", "#", "center", "right", item['DepartmentName']) + ' data-i18n="' + item['PreservingDepartment'] + '">' + item['DepartmentName'] + '</td>\
                        <td ' + Style_cell_Table("100px", "#", "center", "right", item['PreservingTime_Text'].replace('T', ' ')) + '>' + item['PreservingTime_Text'].replace('T', ' ') + '</td>\
                        <td ' + Style_cell_Table("50px", "#", "center", "right", item['Attachment']) + '><i class="fad fa-download f-22 text-success" style="cursor:pointer" onclick="window.open(' + "'/media/" + item['Attachment'] + "', '_blank')" + '"></i></td>\
                </tr>');
            });
            //Alert_OK();
            Reload_Datatable_('table_vanban');
            SHOW_LANG_();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}




//--------------------------------//TẠO ĐƠN XIN MÃ :--------------------------------------------------
//--------------------------------//TẠO ĐƠN XIN PHÁT HÀNH VB :----------------------------------------
//--------------------------------//TẠO ĐƠN XIN HỦY MÃ :----------------------------------------------
//--------------------------------//TẠO ĐƠN XIN HỦY VB :----------------------------------------------


//Thêm thông tin tệp từ modal vào bảng
function Get_file_To_Table(filename) {
    var i = $('#tbody_phuluckemtheo tr').length;
    i += 1;
    $("#tbody_phuluckemtheo").append(
        '<tr i="tr_' + i + '">\
            <td>' + i + '</td>\
            <td ' + Style_cell_Table("230px", "#", "left", "right", $("#DocName").val()) + '>' + $("#DocName").val() + '</td>\
            <td ' + Style_cell_Table("300px", "#", "left", "right", filename) + '><a style="color:#448aff;text-decoration:underline;" href="javascript:void(0);" onclick="window.open(' + "'/static/media/" + filename + "', '_blank')" + '">' + filename + '</a></td>\
            <td ' + Style_cell_Table("90px", "#", "left", "right", $("#CloseDate").val()) + '>' + $("#CloseDate").val() + '</td>\
            <td class="text-center"><i class="far fa-trash-alt f-16" style=" cursor: pointer;" id="bdel_' + i + '" onclick="delete_row(this);"></i><td>\
        </tr>'
    );
    Reload_Tooltip('table_vanban');
    $("#modal_upfilevb").modal('hide');
}



//Upload file đơn lên server
function Up_DonLen_Server() {
    // console.log($('#File_DocRef')[0].files.length);
    if ($("#DocName").val() == '') { Show_Alert_Message('Please Set Document Name !'); return false; }
    if ($('#File_DocRef')[0].files.length <= 0) { Show_Alert_Message('Please select file document !'); return false; }
    if ($("#CloseDate").val() == '') { Show_Alert_Message('Please Set Close Date !'); return false; }
    UPLOAD_FILE_TO_SERVER('File_DocRef', Get_file_To_Table);
}



//Tự động gán mã đơn
function TuDong_SinhMa(id_Document) {
    $("#" + id_Document).val($("#" + id_Document).val() + 'V');
}



//Tạo đơn xin cấp mã hoặc cập nhật đơn cấp mã
function Create_RegisterCode(action) {
    // console.log($('#tbody_phuluckemtheo tr').length);
    if ($('#Department').val() == '') {
        Show_Alert_Message("選擇簽核主管 / Chọn chủ quản ký");
        $('#Department').focus();
        return;
        // } else if ($('#EffectiveDate').val() == '') {
        //     Show_Alert_Message("生效日期/Ngày có hiệu lực??");
        //     return;
    } else if ($('#tbody_phuluckemtheo tr').length < 1) {
        Show_Alert_Message("請登入最少一個資料 / Vui lòng nhập ít nhật 1 tài liệu");
        return;
    }

    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    var i = $('#tbody_phuluckemtheo tr').length;

    var list_docref = $("#tbody_phuluckemtheo tr:has(td)").map(function(index, value) {
        var td = $("td", this);
        return {
            OrderBy: td.eq(0).text(),
            DocumentName: td.eq(1).text(),
            FileName: td.eq(2).text(),
            EstimatedCloseDate: td.eq(3).text()
        }
    }).get();
    data.list_docref = list_docref;
    data.list_docref_length = i;
    // console.log(list_docref)

    var url = '/donxinma/';
    if (action == 'UPDATE') {
        data.action = 'UPDATE';
    } else if (action == 'CREATE') {
        data.action = 'CREATE';
    }
    // console.log(action);
    $.ajax({
        type: 'GET',
        url: url,
        data: data,
        success: function(response) {
            $("#ApplicationNO").val(response['returndata']['CodeDocument']);
            Alert_OK();
            Goto_link_data('chitietdon', 'CodeDocument=' + response['returndata']['CodeDocument']);
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}




//Show modal hủy đơn đăng ký mã
function Show_modal_cancel_regitercode() {
    $("#btn_cancel").removeAttr('hidden');
    $("#btn_appro").prop('hidden', true);
    $("#Modal_Comment").modal('show');
}



//Show modal ký đơn đăng ký mã
function Show_modal_appro_regitercode() {
    $("#btn_appro").removeAttr('hidden');
    $("#btn_cancel").prop('hidden', true);
    $("#Modal_Comment").modal('show');

    //Nếu là DCC sẽ hiển thị thêm tùy chọn

}




//hủy bỏ đơn xin cấp mã
function Cancel_RegisterCode() {
    var data = {
        CodeDocument: $("#ApplicationNO").val(),
        User: $("#Acount_Name").text(),
        Comment: $("#Comment").val()
    };
    $.ajax({
        type: 'GET',
        url: '/cancel_registercode/',
        data: data,
        success: function(response) {
            Alert_OK();
            Goto_link_data('chitietdonxinMVB', 'CodeDocument=' + $("#ApplicationNO").val());
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



//Tìm đơn để hủy mã văn bản
function TimMaDeHuyMaVB() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');

    $.ajax({
        type: 'GET',
        url: '/get_ListRegisterCodeDocumentByDCC/',
        data: data,
        success: function(response) {
            $("#tbody_vanban").empty();
            response['returndata'].forEach(function FILL_DATA(item, index) {
                $("#tbody_vanban").append('<tr>\
                        <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                        <td >' + item['CodeDocument'] + '</td>\
                        <td ><a href="/CreateCancelDocNo/?DocNo=' + item['DocNo'] + '"  style="color:#004aff" id="' + item['DocNo'] + '" >' + item['DocNo'] + '</a></td>\
                        <td>' + item['DocName'] + '</td>\
                        <td>' + item['HoTen'] + '</td>\
                        <td >' + item['Department'] + '</td>\
                        <td >' + item['CreatedDate'].replace('T', ' ') + '</td>\
                    </tr>');
            });
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Lấy thông tin đơn sau khi tạo đơn hủy mã thành công
function Response_Created_CancelCodeDocument(response) {
    $("#CancelDocument").val(response['CancelDocument']);
    Alert_OK();
    if (response['CancelDocument'].lastIndexOf('OP-G') > 0) {
        Goto_Document('chitietdonhuymaVB/?CodeDocument=' + response['CancelDocument']);
    }
}

//Tạo đơn hủy mã văn bản
function TaoDonXinHuyMaVB(Action) {
    var url = '/InsertOrUpdateRegisterCancelDocument/';
    var type = 'GET';
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    data.Action = Action;
    Remind_Question_Ajax(url, type, data, AJAX_REQUEST_RESPONSE, Response_Created_CancelCodeDocument);
}


//Ký duyệt đơn hoặc hủy đơn
function ApproOrCancelDocument(id_Document, Action) {
    function func() {
        Alert_OK;
        $("#Modal_Comment").modal('hide');
        LOAD_PAGE_AGAIN();
    }
    var data = GET_ALL_INPUT_FROM_DIV('Div_modalComment');
    data.Action = Action;
    data.CodeDocument = $("#" + id_Document).val();
    var attr = $("#Div_DCC").attr('hidden');
    if (typeof attr !== typeof undefined && attr !== false) {

    } else {
        if ($("#DocNo").val() == '') { Show_Alert_Message('Chưa có mã văn bản được cấp'); return; }
        if ($("#DocName").val() == '') { Show_Alert_Message('Chưa có tên văn bản'); return; }
    }
    AJAX_REQUEST('/ApproOrCancelDocument/', 'GET', data, func);
}



//Hủy bỏ đơn xin hủy mã văn bản
function sp_CancelRegisterCancelDocument() {
    var data = { CodeDocument: $("#CancelDocument").val() };
    var url = '/CancelRegisterCancelDocument/';
    var type = 'GET';
    Remind_Question_Ajax(url, type, data, AJAX_REQUEST, Alert_OK);
}



//Tìm đơn để phát hành VB
function TimMaDePhatHanh() {
    var url = '/get_ListRegisterCodeDocumentByDCC/';
    var type = 'GET';
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    //Remind_Question_Ajax(url, type, data, AJAX_REQUEST_RESPONSE, FILL_DATA_SEARCH_CodeDocumentByDCC);
    AJAX_REQUEST_RESPONSE(url, type, data, FILL_DATA_SEARCH_CodeDocumentByDCC);
}




function FILL_DATA_SEARCH_CodeDocumentByDCC(response) {
    $("#tbody_vanban").empty();
    response['returndata'].forEach(function FILL_DATA(item, index) {
        $("#tbody_vanban").append('<tr>\
                        <td class="text-center"><i class="fal fa-file-pdf f-18 text-danger" aria-hidden="true"></i></td>\
                        <td >' + item['CodeDocument'] + '</td>\
                        <td ><a href="/CreateCancelDocNo/?DocNo=' + item['DocNo'] + '"  style="color:#004aff" id="' + item['DocNo'] + '" >' + item['DocNo'] + '</a></td>\
                        <td>' + item['DocName'] + '</td>\
                        <td>' + item['HoTen'] + '</td>\
                        <td >' + item['Department'] + '</td>\
                        <td >' + item['CreatedDate'].replace('T', ' ') + '</td>\
                    </tr>');
    });
    //Alert_OK();
}
//--------------------------------//Xác nhận ký đơn:--------------------------------------------------
//--------------------------------//Xác nhận ký đơn:--------------------------------------------------
//--------------------------------//Xác nhận ký đơn:--------------------------------------------------


//Xác nhận ký đơn đăng ký mã
function AcceptRegisterCodeDocument() {

    var data = {
        CodeDocument: $("#ApplicationNO").val(),
        States: '',
        User: $("#Acount_Name").text(),
        Comment: $("#Comment").val()
    };

    $.ajax({
        type: 'GET',
        url: '/duyetdkmavb/',
        data: data,
        success: function(response) {
            $("#Modal_Comment").modal('hide');
            $("#Comment").val('');
            Alert_OK();
            LOAD_PAGE_AGAIN();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}