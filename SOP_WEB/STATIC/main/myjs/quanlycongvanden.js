//----------------------Thực hiện thao tác với công văn đến------------------------

//Thực hiện lấy phòng ban về đơn thực hiện công văn
function Get_Department() {
    function func(response) {
        $("#Donvichusu,#Donvihopban,#Department")
            .empty()
            .append('<option value="" data-i18n=""></option>');
        response['returndata'].forEach(function FILL_DATA(item, index) {
            $("#Donvichusu,#Donvihopban,#Department").append('<option value="' + item['CatCode'] + '" data-i18n="' + item['CatCode'] + '">' + item['CatName'] + '</option>');
            //$("#Donvihopban").append('<option value=' + item['CatCode'] + '>' + item['CatName'] + '</option>');
        });
        SHOW_LANG_();
    }
    AJAX_REQUEST_RESPONSE('/load_Department/', 'GET', 'Department', func);
}


//Thao tác tạo đơn hủy đơn, ký đơn
function TaoYeuCauCongVanDen() {
    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    var Donvichusu = '';
    var Donvihopban = '';
    var filesx = $('#TepscanPDF')[0].files;

    if ($("#Ngaynhanvankien").val() == '') { Show_Alert_Message('Thiếu thông tin ngày nhận văn kiện ! ()'); return; }
    if ($("#Sobiennhan").val() == '') { Show_Alert_Message('Thiếu thông tin số biên nhận !'); return; }
    if ($("#Sovankien").val() == '') { Show_Alert_Message('Thiếu thông tin số văn kiện !'); return; }
    if ($("#Noidungcongvan").val() == '') { Show_Alert_Message('Thiếu nội dung văn kiện !'); return; }
    if ($("#file_PDF").text() == '') { Show_Alert_Message('Thiếu thông tin tệp PDF gửi kèm!'); return; }

    $("#ul_Donvichusu li").each(function() {
        Donvichusu = Donvichusu + $(this).attr('value') + ",";
    });
    $("#ul_Donvihopban li").each(function() {
        Donvihopban = Donvihopban + $(this).attr('value') + ",";
    });

    //if (Donvihopban == '') { Show_Alert_Message('Thiếu thông tin đơn vị phụ trách !'); return; }
    //if (Donvihopban == '') { Show_Alert_Message('Thiếu thông tin đơn vị hỗ trợ !'); return; }


    //var TepscanPDF = filesx[0].name;
    TepscanPDF = $("#file_PDF").text();
    data.TepscanPDF = TepscanPDF;
    data.Donvichusu = Donvichusu;
    data.Donvihopban = Donvihopban;
    data.Tepvbtraloi = $("#file_vbtraloi").text()
        //console.log(data);

    function func(response) {
        $("#Sodon").val(response['returndata']);
        Alert_OK();
        $("#Div_btnCreateArr").remove();
    }
    AJAX_REQUEST_RESPONSE('/taoyeucaucv/', 'GET', data, func);

}



//Duyệt công văn
function DuyetCongVan() {
    //alert('Chức năng Duyệt công văn');
    function func(response) {
        $("#tbody_Waiting").empty();
        Reset_Table_Datatable('tbl_Waiting');
        var num = 0;
        response['returndata'].forEach(function FILL_DATA(item, index) {
            var Status = item['Status'];
            num += 1;
            if (Status == 'Waiting') { Status = '<i class="fal fa-paper-plane f-16 text-success"></i>' } else { Status = '<i class="fal fa-envelope f-16 text-danger"></i>' }
            $("#tbody_Waiting").append('<tr>\
            <td>' + num + '</td>\
            <td><a href="javascript:void(0)" onclick="ChiTietDon_CVD(this)" style="color:#004aff" id="' + item['Sodon'] + '">' + item['Sodon'] + '</a></td>\
            <td>' + item['Sovankien'] + '</td>\
            <td>' + item['Nguoitrinhdon'] + '</td>\
            <td>' + GET_STRING_DATETIME1(item['NgaytrinhkyGD']) + '</td>\
            <td data-i18n="' + item['Status'] + '">' + item['Status'] + '</td>\
            <td>' + Status + '</td>\
            </tr>');
        });
        Reload_Datatable_('tbl_Waiting');
    }
    AJAX_REQUEST_RESPONSE('/duyet_CVD/', 'GET', '', func);
}



//Tạo yêu cầu công văn đến
function TraCuuCongVan() {
    // alert('Chức năng tra cứu công văn');
    var data = GET_ALL_INPUT_FROM_DIV('Div_search');
    var num = 0;

    function func(response) {
        $("#tbody_Congvanden").empty();
        Reset_Table_Datatable('tbl_Congvanden');
        response['returndata'].forEach(function FILL_DATA(item, index) {
            num += 1;
            var Status = item['Status'];
            if (Status == 'Waiting') { Status = '<i class="fal fa-paper-plane f-16 text-success"></i>' } else { Status = '<i class="fal fa-envelope f-16 text-danger"></i>' }
            $("#tbody_Congvanden").append('<tr>\
            <td class="text-center">' + num + '</td>\
            <td class="text-center" style="max-width:300px !important"><a href="javascript:void(0)" onclick="ChiTietDon_CVD(this)" style="color:#004aff" id="' + item['Sodon'] + '">' + item['Sodon'] + '</a></td>\
            <td class="text-center">' + item['Sovankien'] + '</td>\
            <td class="text-center">' + GET_STRING_DATETIME1(item['NgaytrinhkyGD']) + '</td>\
            <td class="text-center">' + item['Status'] + '</td>\
            <td>' + Status + '</td>\
            </tr>');
        });
        //Alert_OK();
        Reload_Datatable_('tbl_Congvanden');
    }
    AJAX_REQUEST_RESPONSE('/search_SOP_H/', 'GET', data, func);
}



//Lấy thông tin chi tiết công văn đến
function ChiTietDon_CVD(element) {
    var code = $(element).text();
    var href = 'chitietdon_CVD/?Sodon=' + code;
    Open_link(href, '_self');
}



//Hiển thị modal ký công văn đến
function Show_Modal_Appro(Action) {
    $("#btn_xacnhan").attr('onclick', "Ky_CongVanDen('" + Action + "')");
    $('#Modal_Comment').modal('show');
}



//Ký duyệt công văn
function Ky_CongVanDen(Action) {

    var data = GET_ALL_INPUT_FROM_DIV('Div_area');
    data.Action = Action;
    var Donvichusu = '';
    var Donvihopban = '';
    var TenDonvichusu = '';
    var TenDonvihopban = '';

    $("#ul_Donvichusu li").each(function() {
        Donvichusu += $(this).attr('value') + ",";
        TenDonvichusu += "<li>" + $(this).children('span').text() + "</li><br/>";
    });
    $("#ul_Donvihopban li").each(function() {
        Donvihopban += $(this).attr('value') + ",";
        TenDonvihopban += "<li>" + $(this).children('span').text() + "</li><br/>";
    });

    data.Donvichusu = Donvichusu;
    data.Donvihopban = Donvihopban;
    data.TenDonvichusu = TenDonvichusu;
    data.TenDonvihopban = TenDonvihopban;

    if (Donvichusu == '' || Donvihopban == '' || $("#Donvikhac").val == '') {
        Show_Alert_Message('Chưa chọn đơn vị thực hiện ! (未選定實施單位)');
        $("#Modal_Comment").modal('hide');
        return
    }

    var file_vbtraloi = $("#file_vbtraloi").text();
    var Comment = $("#Comment").val();
    data.file_vbtraloi = file_vbtraloi;
    data.Comment = Comment;
    //console.log(data);
    AJAX_REQUEST('/Appro_SOP_H/', 'GET', data, LOAD_PAGE_AGAIN);
}




//Upload file PDF lên server
function Upload_PDF() {
    function func(namefile) {
        //console.log(namefile);
        $("#file_PDF")
            .attr('onclick', "window.open('/static/media/" + namefile + "', '_blank')")
            .text(namefile);
        Alert_OK();
    }
    var filePDF = UPLOAD_FILE_TO_SERVER('TepscanPDF', func);
}



//Upload văn bản trả lời
function Upload_VBTRALOI() {
    function func(namefile) {
        //console.log(namefile);
        $("#file_vbtraloi")
            .attr('onclick', "window.open('/static/media/" + namefile + "', '_blank')")
            .text(namefile);
        Alert_OK();
    }
    var filePDF = UPLOAD_FILE_TO_SERVER('Tepvbtraloi', func);
}



//ẩn hiện mục upload văn bản trả lời
function Show_Hide_uploadvbtraloi(element) {
    if ($(element).attr('value') == 1) {
        $("#Div_chonvbtraloi").removeAttr('hidden');
        $("#Div_btnvbtraloi").removeAttr('hidden');
        $("#Div_tenvbtraloi").removeAttr('hidden');
    } else {
        $("#Div_chonvbtraloi").prop('hidden', true);
        $("#Div_btnvbtraloi").prop('hidden', true);
        $("#Div_tenvbtraloi").prop('hidden', true);
    }
}



//Hiển thị mục chọn đơn vị khác
function Show_Hide_Dovikhac(element) {
    if ($(element).attr('value') == 1) {
        $("#Div_Donvikhac").removeAttr('hidden');
    } else {
        $("#Div_Donvikhac").prop('hidden', true);
    }
}