//Local variable
var FormName = '';
urlstatic_JS = $("#urlstatic_JS").text();



//Đường dẫn hình ảnh cho ảnh thẻ
var urlimg = '/static/images/blank.jpg';
var urlimg2 = '/static/media/';

//Thông tin CSRFTOKEN
var csrf_name = '';
var csrf_value = '';

var mydate = new Date;


//Hỏi trước khi thực hiện
function CONFIRM_Question() {
    let text = "Are you sure ??";
    if (confirm(text) == true) {
        return true;
    } else {
        return false;
    }
}




//Load danh sách menu
function LOAD_OPTION() {
    var option_typeUsecar = '<option selected="selected" value="D" data-i18n="duanhanviendi">Đưa nhân viên đến và rời khỏi nơi làm việc</option>\
                      <option value="B" data-i18n="giamsatchuyenhuong">Người giám sát chuyển nhượng cố định</option>\
                      <option value="A" data-i18n="donnguoitaisb">Đón người tại sân bay</option>\
                      <option value="P" data-i18n="duanguoirasb">Đưa người ra sân bay</option>\
                      <option value="E" data-i18n="duadonhn">Thường xuyên đưa đón nhân viên đi và về tại Hà Nội</option>\
                      <option value="F" data-i18n="muasamhn">Đi mua sắm ở hà nội</option>\
                      <option value="G" data-i18n="donvatrak">Đón và trả khách</option>\
                      <option value="H" data-i18n="congvantamthoi" hidden>Công văn tạm thời</option>\
                      <option value="I" data-i18n="xeduadoncd">Xe đưa đón cố định</option>\
                      <option value="C" data-i18n="giaobuaan">Giao bữa ăn cố định</option>\
                      <option value="J" data-i18n="nhanthe">Nhận thẻ tình bạn</option>\
                      <option value="K" data-i18n="donsinhvien">Đón sinh viên đại học</option>\
                      <option value="L" data-i18n="lamnhiemvu">Làm nhiệm vụ</option>\
                      <option value="P" data-i18n="thue16cho">Cho thuê xe 29 chỗ</option>\
                      <option value="M" data-i18n="thue29cho">Cho thuê xe 29 chỗ</option>\
                      <option value="N" data-i18n="thue45cho">Cho thuê xe 45 chỗ</option>\
                      <option value="O" data-i18n="Dongxing">Dongxing Pass</option>';

    var option_route = '<option value="A" data-i18n="tpbacning">Thành phố Bắc Ninh</option>\
                      <option value="B" data-i18n="tpbacgiang">Bắc Giang</option>\
                      <option value="C" data-i18n="hanoi">Hà nội</option>\
                      <option value="D" data-i18n="duongdai">Đường dài</option>';

    var option_yn = '<option value="N" data-i18n="khong">Không</option>\
                  <option value="Y" data-i18n="co">Có</option>';

    var option_cartype = '<option value="A" data-i18n="xecongvu">Xe công vụ</option>';

    var option_Statusdoc = '<option value="" data-i18n="all">Tất cả</option>\
                        <option value="Completed" data-i18n="Completed">Đồng ý cấp đi</option>\
                        <option value="Rejected" data-i18n="Rejected">Từ chối gửi xe</option>\
                        <option value="Pending" data-i18n="Pending">Chưa xử lý</option>\
                        <option value="Canceled" data-i18n="Canceled">Đã hủy</option>';

    var option_typecar = ' <option value="0" data-i18n="xekinhdoanh">Xe kinh doanh</option>\
                        <option value="1" data-i18n="xetaxi">Xe taxi</option>\
                        <option value="2" data-i18n="xechothue">Xe cho thuê</option>';



    var option_classcar = ' <option value="" data-i18n="all">球車證</option>\
                          <option value="A" data-i18n="bangA">A類</option>\
                          <option value="B" data-i18n="bangB">B類</option>\
                          <option value="C" data-i18n="bangC">C類</option>\
                          <option value="D" data-i18n="bangD">D類</option>\
                          <option value="E" data-i18n="bangE">E類</option>\
                          <option value="B2" data-i18n="bangB2">B2類</option>\
                          <option value="A1,D" data-i18n="bangA1D">A1,D類</option>';

    var option_sex = '<option value=""></option>\
                   <option value="M" data-i18n="nam">男</option>\
                   <option value="F" data-i18n="nu">女</option>';

    $("#CARD_TYPE")
        .empty()
        .append(option_classcar);

    $("#DRIVER_SEX")
        .empty()
        .append(option_sex);


    $("#cbx_typeusecar")
        .empty()
        .append(option_typeUsecar);
    $("#TYPE_USECAR1")
        .empty()
        .append(option_typeUsecar);



    $("#cbx_route")
        .empty()
        .append(option_route);
    $("#ROUTE1")
        .empty()
        .append(option_route);


    $("#cbx_parking")
        .empty()
        .append(option_yn);

    $("#CAR_TYPE21")
        .empty()
        .append(option_typecar);


    $("#cbx_cartype")
        .empty()
        .append(option_cartype);
    $("#CAR_TYPE1")
        .empty()
        .append(option_cartype);



    $("#cbx_behalf")
        .empty()
        .append(option_yn);

    $("#STATUS_DOC")
        .empty()
        .append(option_Statusdoc);

    $("#cbx_behalf")
        .empty()
        .append(option_yn);

    $("#CAR_POOLING1")
        .empty()
        .append(option_yn);


}

//Hàm trả về biểu tượng của trạng thái đơn
function SHOW_FLAG_STATUS(STATUS_DOC, size_icon) {
    var FLAG = ''
    if (STATUS_DOC == "Waiting") {
        FLAG = '<i id="btn_" class="fal fa-paper-plane ' + size_icon + ' text-c-green" style="cursor: pointer;" onclick=""></i>';
    } else if (STATUS_DOC == "Pending") {
        FLAG = '<i id="btn_" class="fal fa-envelope ' + size_icon + ' text-c-green" style="cursor: pointer;" onclick=""></i>';
    } else if (STATUS_DOC == "Completed") {
        FLAG = '<i id="btn_" class="fas fa-envelope ' + size_icon + ' text-c-green" style="cursor: pointer;" onclick=""></i>';
    } else if (STATUS_DOC == "Canceled") {
        FLAG = '<i id="btn_" class="fas fa-ban ' + size_icon + ' text-c-red" style="cursor: pointer;" onclick=""></i>';
    } else if (STATUS_DOC == "Rejected") {
        FLAG = '<i id="btn_" class="fa fa-recycle ' + size_icon + ' text-c-blue" style="cursor: pointer;" onclick=""></i>';
    } else { FLAG = '<i class="fas fa-question ' + size_icon + '"></i>'; }
    return FLAG;
}




//Phương thức ajax xử lý dữ liệu từ server
function AJAX_REQUEST(url, type, data, func) {
    $.ajax({
        type: type,
        url: url,
        data: data,
        success: function(response) {
            func();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}

//Phương thức ajax xử lý dữ liệu từ server với 1 tham số 
function AJAX_REQUEST_PARAM(url, type, data, func, param) {
    $.ajax({
        type: type,
        url: url,
        data: data,
        success: function(response) {
            func(param);
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}


//Phương thức ajax xử lý dữ liệu từ server
function AJAX_REQUEST_RESPONSE(url, type, data, func) {
    $.ajax({
        type: type,
        url: url,
        data: data,
        success: function(response) {
            func(response);
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}

//Phương thức ajax POST xử lý dữ liệu từ server
function AJAX_POST_REQUEST_RESPONSE(url, formdata, func) {
    $.ajax({
        type: 'POST',
        url: url,
        data: formdata,
        contentType: false,
        processData: false,
        headers: { "X-CSRF-Token": formdata['csrf_value'] },
        success: function(response) {
            func(response);
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}

//Hàm chỉ cho nhập vào số
function ONLY_NUMBER_INPUT(element) {
    $(element).keyup(function(e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value.replace(/\D/g, '');
        }
    });
}


//lấy thông tin truyền hình ảnh vào formdata 
function GET_FORM_DATA_TO_POST(photo) {
    if (photo.name == '') {
        Show_Alert_Message("Chưa có file được chọn !");
        e.preventDefault()
    }

    // Sử dụng jquery:
    var formData = new FormData($('#frm_formfile')[0]);
    //Lấy mã csrftocken gán vào Formdata
    $("#frm_csftk").each(function() {
        if ($(this).find(':input')) {
            btn = $(this).find(':input');
            csrf_name = $(btn).attr('name');
            csrf_value = $(btn).attr('value');
            formData.append(csrf_name, csrf_value);
        }
    });

    var files = photo;
    // if (files.name.indexOf("+") > 0) {
    //     alert("Name file error '+'");
    //     e.preventDefault();
    // }
    formData.append('myfile', files);
    formData.append('file_length', 1);
    return formData;
}



//lấy thông tin truyền hình ảnh vào formdata 
function GET_FORM_DATA_TO_POST(id_inputFile) {
    var x = document.getElementById(id_inputFile);
    var file = '';
    if ('files' in x) {
        if (x.files.length == 0) {
            //kHÔNG CÓ FILE ĐƯỢC CHỌN
            Show_Alert_Message("Chưa có file được chọn !");
            e.preventDefault()
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
            //kHÔNG CÓ FILE ĐƯỢC CHỌN
            Show_Alert_Message("Chưa có file được chọn !");
            e.preventDefault()
        } else {
            // If the browser does not support the files property, it will return the path of the selected file instead. 
        }
    }


    // Sử dụng jquery:
    var formData = new FormData($('#frm_formfile')[0]);
    //Lấy mã csrftocken gán vào Formdata
    $("#frm_csftk").each(function() {
        if ($(this).find(':input')) {
            btn = $(this).find(':input');
            csrf_name = $(btn).attr('name');
            csrf_value = $(btn).attr('value');
            formData.append(csrf_name, csrf_value);
        }
    });


    // if (file.name.indexOf("+") > 0) {
    //     alert("Name file error '+'");
    //     e.preventDefault();
    // }
    formData.append('myfile', file);
    formData.append('file_length', 1);
    return formData;
}



//Lọc menu tìm kiếm DROPDOWN vơi input text
function filterFunction(id_input, id_dropmenu) {
    var input, filter, ul, li, a, i;
    input = document.getElementById(id_input);
    filter = input.value.toUpperCase();
    div = document.getElementById(id_dropmenu);
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}


//Lấy dữ liệu từ menu dropdownMenuButton truyền vào 1 input id
function GET_TEXT_MENU(element, id_settext) {
    $("#" + id_settext).val($(element).text());
    $("#" + id_settext).focus();
}


//Lấy toàn bộ ID và value của ID đưa vào object
function GET_ALL_INPUT_FROM_DIV(id_DIV) {
    var data = {}
    $("#" + id_DIV + " :input").each(function() {
        data[$(this).attr('id')] = $(this).val();
    });
    return data;
}


//Lấy toàn bộ ID và value của ID đưa vào object
function GET_ALL_INPUT_FROM_MODAL(modal_id) {
    var data = {}
    $("#" + modal_id + " :input").each(function() {
        var id = $(this).attr('id');
        if (id != undefined) {
            id = id.substring(0, id.length - 1);
            data[id] = $(this).val();
        }
    });
    return data;
}



//Kiểm tra có tệp có phải là ảnh hay không
function CHECK_IMAGE_FILE(element) {
    var photo = $(element)[0].files[0];
    // alert(photo.name);
    var validImageTypes = ['image/gif', 'image/jpeg', 'image/png', 'image/bmp'];
    var fileType = photo['type'];
    if (!validImageTypes.includes(fileType)) {
        alert("Not Image File, check again!");
        return false;
    }
    return true;
}



//Hàm kiểm tra dữ liệu
function CHECK_ARR_NOT_NULL(arr) {
    var check = true;
    $.each(arr, function(index, value) {
        if (value == "") {
            // console.log("Giá trị trống :" + index);
            alert("Bạn thiếu thông tin :" + index);
            check = false;
            return false;
        }
    });
    // alert('OK');
    return check;
}



//RESET trống thông tin của các thẻ con trong thẻ cha
function RESET_AREA(id_area) {
    $("#" + id_area).each(function() {
        $(this).val('');
        var button = $(this).find(':input');
        $(button).val('');
        $(button).prop('checked', false);
        var button1 = $(this).find('select');
        $(button1).val('');
        var button2 = $(this).find('textarea');
        $(button2).val('');

    });
}


//Ẩn tất cả các button trong thẻ div
function Hide_All_Button_FromDiv(id_DIV) {
    $("#" + id_DIV).each(function() {
        $(this).find(":button").parent().prop('hidden', true);
    });
}


//Loại bỏ các thuộc tính hidden trong các thẻ button của thẻ DIV cha
function Remove_Attr_Hidden_Button_FromDiv(id_DIV) {
    $("#" + id_DIV).each(function() {
        $(this).find(":button").parent().removeAttr('hidden');
    });
}


// yourInterval = setInterval(function() {
//     GET_ALL_INFOR_DOCNO();
//     $('#timer1').text((new Date - mydate) / 1000 + " Seconds");
// }, 60000);


//Lấy toàn bộ ID và value Checkbox được checked đưa vào object và bỏ phần check_
function GET_CHECKED_CHECKBOX_FROM_DIV(id_DIV) {
    var data = {}
    $("#" + id_DIV + " :input").each(function() {
        if ($(this).is(":checked")) {
            data[$(this).attr('id').substring($(this).attr('id'))] = $(this).val();
        }
    });
    return data;
}


//Load file HTML vào html:
function Load_html_1(id_DIV, path_html) {
    $("#" + id_DIV).load(path_html, function() {
        SHOW_LANG_();
    });

}

//Load lại trang
function LOAD_PAGE_AGAIN() {
    location.reload();
}

//Kiểm tra trình duyệt có phải IE
function CHECK_IE() {
    var isIE = window.ActiveXObject || "ActiveXObject" in window;
    //<!--Nếu  là  IE js -->
    if (isIE) {
        return true;
        //<!--Nếu Không phải là  IE js -->
    } else {
        return false;
    }
}


//Hiển thị Modal thông qua ID
function Show_Modal_FromID(id_modal) {
    $("#" + id_modal).modal('show');
}
//Đóng Modal thông qua ID
function Close_Modal_FromID(id_modal) {
    $("#" + id_modal).modal('hide');
}



//Checkbox thay đổi toàn bộ các checkbox khác
function CHECKBOX_CHANGE_ALL(id_checkbox, id_Area) {
    $("#" + id_checkbox).change(function() {
        if ($(this).is(":checked")) {
            $("#" + id_Area + " :input").each(function() {
                $(this).prop('checked', true);
            });
        } else {
            $("#" + id_Area + " :input").each(function() {
                $(this).prop('checked', false);
            });
        }
    })
}




//Show modal loadding
function Show_loading() {
    $("#modal-loading").modal('show');
}
//Countdown thoát Loading
function Exit_Loading() {
    // Update the count down every 1 second
    var x = setInterval(function() {
        $("#modal-loading").modal('hide');
    }, 1000);
}





//Tự động binding dữ liệu từ oject về các thẻ ID
function BINDING_DATA_TO_ID(oject) {
    // for (var [key, value] of Object.entries(oject)) {
    //     $("#" + key).val(value);
    //     console.log(key);

    // }
    //console.log(oject);

    // for (var key in oject) {
    //     console.log("key " + key + " has value " + oject[key]);
    // }


    // console.log(oject);
    $.each(oject, function(key, value) {
        $("#" + key).val(value);
    });

}


//Thêm xe vào đơn đưa đón chủ quản
function DROPDOWN_GET_SELECT_CAR(element, id_input) {
    var text = $(element).text();
    $("#" + id_input).val(text);
    $(element).parent('div').removeClass('show');
}

//Hiển thị dropdown khi nhấn vào input
function SHOW_DROPDOWN_FROM_INPUT(id_input, id_dropdown) {
    $("#" + id_input).click(function() {
        if ($('#' + id_dropdown).hasClass('show')) {
            $('#' + id_dropdown).removeClass('show');
            $('#' + id_dropdown).focus();
        } else {
            $('#' + id_dropdown).addClass('show');
        }
    });
    $("#" + id_input).focusout(function() {
        $('body').click(function(e) {
            var target = $(e.target);
            if (target.is('#' + id_dropdown) || target.is("#" + id_input)) { return; } else {
                ($('#' + id_dropdown).removeClass('show'))
            }
        });
    });
}


//Nhấn nút hủy bỏ
function BACK_HOME() {
    choice = '';
    // var hostname = "https://" + window.location.host + "/"
    var host = window.location.protocol + "//" + window.location.host;
    var hostname = window.location = host + "/home/"
    window.location.assign(hostname);
    window.location = hostname;
    window.location.href = hostname;
}


function create_app(but) { //create application
    //khai báo dữ liệu

    $("#modal-delete-row1").modal();
    $("#btn_save").click(function() {
        //do something
        $('#modal-delete-row1').modal('hide');
    });
}

// Hiển thị ảnh cá nhân
function show_icon_user() {

    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/show_icon_user/",
        data: 'me',

        success: function(response) {
            var str = JSON.stringify(response["returndata"]);
            var arrdic = JSON.parse(str);
            var fields = arrdic;
            var img = fields.img;
            d = new Date();
            if (img == null) {


                $("#img_avatar").removeAttr('src')
                    .removeAttr('src')
                    .prop('src', urlstatic_JS + 'img/pen.jpg' + "?" + d.getTime());

                $("#img_profile")
                    .removeAttr('src')
                    .prop('src', urlstatic_JS + 'img/pen.jpg' + "?" + d.getTime());

            } else {

                $("#img_avatar").removeAttr('src')
                    .removeAttr('src')
                    .prop('src', urlimg2 + img + "?" + d.getTime());

                $("#img_profile")
                    .removeAttr('src')
                    .prop('src', urlimg2 + img + "?" + d.getTime());

            }
        },
        error: function(response) {
            // alert the error if any error occured
            AlertErrorSQL(response);
        }
    })
}


//------------------------------------------------------------FORM NAME SETTING--------------------------------------------------------
$(document).ready(function() {


    // Sự kiện enter input text
    // $("#txt_title").keypress(function(event) {
    //     var keycode = (event.keyCode ? event.keyCode : event.which);
    //     if (keycode == '13') {
    //         location = "?flowtitle=" + $("#txt_title").val();
    //     }
    // });
    //sự kiện thay đổi href khi nhấn input text
    //     $("#txt_title").keydown(function() {
    //         var data = $("#txt_title").val();
    //         $("#btn_tk4").prop("href", "/formnamesetting/?flowtitle=" + data);
    //     });
    //     $("#txt_title").keyup(function() {
    //         var data = $("#txt_title").val();
    //         $("#btn_tk4").prop("href", "/formnamesetting/?flowtitle=" + data);
    //     });
});



function Query_Docno(docno) {

    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/find_part_docno/",
        data: {
            docno: docno
        },
        success: function(response) {
            response["returndata"].forEach(function myFunctionx(item, index1) {
                nonum += 1;
                $("#tbody_query").append(
                    '<tr  class="clickable-row">\
                    <td id="ID_' + item["Apply_No"] + '">' + nonum + '</td>\
                    <td id="Apply_No_' + item["Apply_No"] + '"><a id="DG_base_link_Apply_No_0" href="#" style="color:Blue;text-decoration:underline;">' + item["Apply_No"] + '</a></td>\
                    <td id="Level_Grade_' + item["Apply_No"] + '">' + item["Level_Grade"] + '</td>\
                    <td class="text-left" id="Apply_File_' + item["Apply_No"] + '" class="text-left"><a  href="javascript:void(0);" style="color:Blue;text-decoration:underline;">' + item["Apply_File"].substring(14) + '</a><br></td>\
                    <td class="text-left" id="Attem_File_' + item["Apply_No"] + '"></td>\
                    <td id="Apply_Person_' + item["Apply_No"] + '">' + item["Apply_Person"] + '</td>\
                    <td id="Status_' + item["Apply_No"] + '">' + item["Process"] + '</td>\
                    <td id="Sign_Type_' + item["Apply_No"] + '">' + item["Sign_Type"] + '</td>\
                    <td id="Signer_' + item["Apply_No"] + '">' + item["Next_Name"] + '</td>\
                    <td class="text-center">\
                        <i id="btn_edit_approver_' + item["Apply_No"] + '"  class="fas fa-edit "  style="cursor: pointer;" onclick="edit_approver(this);"></i><i class="fas ">&nbsp;&nbsp;</i>\
                        <i id="btn_del_approver_' + item["Apply_No"] + '"  class="fas fa-trash-alt"  style="cursor: pointer;" onclick="delete_approver(this);"></i>\
                    </td>\
                  </tr>');
                Show_Attem_FileDocno(item["Apply_No"]);
                //Show_Waiting_Approver(item["Apply_No"]);
            });
        },
        error: function(response) {
            // alert the error if any error occured
            AlertErrorSQL(response);
        }
    })
}



//Hiển thị thông tin chi tiết đơn vào form docdetail
function Doc_Detail(el) {
    var docno = $(el).text();
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/doc_detail/?docno=' + docno
        // window.open(newhref, '_blank'); //Mở 1 tab mới
        // window.open(newhref);
    window.location = newhref;
}



//Về trang chờ ký
function Go_TO_WaitingApprove() {
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/waittingdoc/'
    window.location = newhref;
}



// //Hiển thị các file upload đính kèm
function Show_Attem_FileDocno1(doc) {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/show_attem_file_upload/",
        data: {
            docno: doc
        },
        success: function(response) {
            response["returndata"].forEach(function myFunctionx(item, index1) {
                $("#Attem_File_" + doc).prepend('<a href="javascript:void(0);">' + item["File_Name"].substring(14) + '</a><br>');
            });
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//Hiển thị các file upload đính kèm
function Show_Attem_FileDocno(doc) {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/show_attem_file_upload/",
        data: {
            docno: doc
        },
        success: function(response) {
            response["returndata"].forEach(function myFunctionx(item, index1) {
                $("#Attem_File_" + doc).prepend(
                    '<a href="javascript:void(0);" style="color:#448aff;text-decoration:underline;">' + item["File_Name"].substring(14) + '</a><br>\
                    ');
            });
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//HÀM GỬI MAIL TỰ ĐỘNG các mail cách nhau dấu ,
function WMSendMail(mailto, mailfrom, cc, subject, message) {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "http://10.224.69.51/SMTPService/SMTPService.asmx/WMSendMail?mailto=" + mailto + "&from=" + mailfrom + "&cc=" + cc + "&subject=" + subject + "&msg=" + message + "",
        data: ''
            // success: function(response) {
            //     Alert_OK();
            // },
            // error: function(response) {
            //     alert(JSON.stringify(response));
            //     AlertErrorSendMail();
            // }
    })
}



//TEst gửi mail
function TestMail() {
    var mailto = 'cncs-vn-code@mail.foxconn.com';
    var mailfrom = 'cncs-vn-code@mail.foxconn.com';
    var cc = 'cncs-vn-code@mail.foxconn.com';
    var subject = 'E_Sign 4.0';
    var message = 'Test send mail by ajax';
    message = message;
    WMSendMail(mailto, mailfrom, cc, subject, message);
}



//Đăng xuất tài khoản
function LogOut() {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/logout/",
        data: '',
        success: function(response) {
            location.reload();
            // var host = window.location.protocol + "//" + window.location.host;
            // var newhref = host + '/login/'
            // window.location = newhref;
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//Tải file từ server về
function Donwload_File(element) {
    var filename = $(element).text();
    // alert('msg');
    downloadFile(filename);
}



//Hàm tải file
function downloadFile(fname) {

    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/download_file/",
        data: { "lstfile": fname },
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {

            // download the file
            var link = document.createElement('a'),
                filename = fname;
            link.href = URL.createObjectURL(data);
            link.download = filename;
            link.click();

            // alert(link.href);
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//Hàm tải file
function downloadFile_PDF_Merge(file1, file2, fname) {
    var data = {
            file1: file1,
            file2: file2,
            PDF_MERGE: fname
        }
        // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/download_PDF_merge/",
        data: data,
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {
            var link = document.createElement('a'),
                filename = fname;
            link.href = URL.createObjectURL(data);
            link.download = filename;
            link.click();
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}


//Hàm lấy thông tin HOSTNAME
function GET_HOSTNAME() {
    var host = window.location.protocol + "//" + window.location.host;
    // var hostname = window.location = host
    return host;
}



//Hàm trả về chuỗi thời gian dd-mm-yyy h:m
function GET_STRING_DATETIME1(dateString) {
    if (dateString === null) { return ''; }
    const d = new Date(dateString);
    let y = d.getFullYear();
    let mm = d.getMonth();
    let dd = d.getDate();
    let h = d.getHours();
    let m = d.getMinutes();
    let s = d.getSeconds();
    var ampm = h >= 12 ? 'PM' : 'AM';
    today = y + "-" + mm + "-" + dd + " " + h + ":" + m + ampm;
    return today;
}


//Hàm trả về chuỗi thời gian yyyy-mm-dd hh:m
function GET_STRING_DATETIME2(dateString) {
    if (dateString === null) { return ''; }
    dateString = dateString.replace("T", ' ');
    dateString = ReplaceAll(dateString, "-", '/');
    dateString = dateString.substring(0, dateString.length - 4)
    return dateString;
}




//API regex replace all
function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}

function ReplaceAll(str, find, replace) {
    if (str === null || str === undefined) { return "" }
    return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
}



//Hàm trả về thông tin các đơn đang chờ ký
function SHOW_DOC_Notifications() {

    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/Waiting_approver/",
        data: {
            docno: ''
        },
        success: function(response) {

            var lang = getcookie_lang();

            if (lang.length <= 0) { lang = "en"; }
            var noti = '',
                op = '';
            if (lang == 'vn') {
                noti = 'Thông báo';
                op = "Mới";
            } else if (lang == 'en') {
                noti = 'Notifications';
                op = 'New';
            } else if (lang == 'cn') {
                noti = '通知';
                op = '新的'
            }


            $("#Show_docnolist")
                .empty()
                .append(
                    '<li>\
            <!-- MENU SHOW ICON -->\
            <h6>' + noti + '</h6>\
            <label class="label label-warning">' + op + '</label>\
          </li>');

            $(".badge").removeClass("bg-c-yellow"); //Xóa thông báo khi không có đơn ký

            response["returndata"].forEach(function myFunctionx(item, index) {
                var Level_Grade = item["Level_Grade"];
                Level_Grade = Level_Grade == 'Urgent' ? '<label class="label label-danger text-white">Urgent' : '<label class="label label-info text-white">Normal';
                var img = item['img'];

                $(".badge").addClass("bg-c-yellow"); //Tô màu thông báo có đơn 

                if (img == null) {
                    $("#Show_docnolist").append(
                        '<li class="waves-effect waves-light">\
                        <div class="media">\
                            <img class="d-flex align-self-center img-radius" src="' + urlstatic_JS + 'img/pen.jpg" alt="User image">\
                            <div class="media-body">\
                                <h5 class="notification-user">' + item["Apply_Person"] + '_' + item["Apply_EmpNo"] + '</h5>\
                                <p class="notification-msg"><a href="javascript:void(0);" onclick="Doc_Detail(this);"  style="color:#448aff;text-decoration:underline;">' + item["Apply_No"] + '</a></p>\
                                <span class="notification-time">At: ' + GET_STRING_DATETIME1(item["Edit_Time"]) + '</span>\
                            </div>\
                            ' + Level_Grade + '</label>\
                        </div>\
                    </li>\
                    ');
                } else {
                    $("#Show_docnolist").append(
                        '<li class="waves-effect waves-light">\
                        <div class="media">\
                        <img class="d-flex align-self-center img-radius" src="' + urlstatic_JS + 'media/' + img + '" alt="User image">\
                        <div class="media-body">\
                                <h5 class="notification-user">' + item["Apply_Person"] + '_' + item["Apply_EmpNo"] + '</h5>\
                                <p class="notification-msg"><a href="javascript:void(0);" onclick="Doc_Detail(this);"  style="color:#448aff;text-decoration:underline;">' + item["Apply_No"] + '</a></p>\
                                <span class="notification-time">At: ' + GET_STRING_DATETIME1(item["Edit_Time"]) + '</span>\
                            </div>\
                            ' + Level_Grade + '</label>\
                        </div>\
                    </li>\
                    ');
                }
            });
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}


//Hàm phân quyền cho các module
function GET_perMission_module(idModule) {
    $('Div[name*="' + idModule + '"],ul[name*="' + idModule + '"],li[name*="' + idModule + '"]')
        .removeAttr('hidden')
        .removeAttr('style');

}


//Hàm Phân quyền User các module
function PERMISSION_USER() {
    AJAX_REQUEST_RESPONSE('/show_permission/', 'GET', 'data', func);

    function func(response) {
        response['returndata'].forEach(function(item, index) {
            GET_perMission_module(item['Groups_Menu']);
            GET_perMission_module(item['Code_Menu']);
        });
    }
}


//Checkbox thay đổi giá trị khi tích chọn
function SetValue_CheckBox(element) {
    if ($(element).is(":checked")) { $(element).prop('value', '1') } else { $(element).prop('value', '0') }
}


//Xóa row trong bảng
function delete_row(element) {
    $(element).closest("tr").remove();
}

//Load lại tooltip với datatable
function Reload_Datatable_(id_table) {
    $("#" + id_table)
        .DataTable()
        .on('draw', function() {
            $('[data-toggle="tooltip"]').tooltip({
                html: true,
            });
        });
}


function Reload_Tooltip(id_table) {
    $("#" + id_table)
        .on('draw', function() {
            $('[data-toggle="tooltip"]').tooltip({
                html: true,
            });
        });
}


//Xóa bảng và hủy phân trang của bảng
function Reset_Table_Datatable(id_table) {
    $("#" + id_table).DataTable().destroy();
    $("#" + id_table + ">tbody").empty();
}

//Di chuyển modal :
function Move_modal(id_modalDialog) {
    $("#" + id_modalDialog).draggable();
}


//In chữ ký màu của thẻ Div
function printDiv(divName) {
    $("#show_pdf").text('Show PDF');
    $("#list_upload iframe").remove();
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


//In chữ ký đen trắng của thẻ Div
function PrintElem(elem) {
    var mywindow = window.open('', 'PRINT', 'height=400,width=600');

    mywindow.document.write('<html><head><title>' + document.title + '</title>');
    mywindow.document.write('</head><body >');
    //mywindow.document.write('<h1>' + document.title + '</h1>');
    mywindow.document.write(document.getElementById(elem).innerHTML);
    mywindow.document.write('</body></html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/

    mywindow.print();
    mywindow.close();

    return true;
}



//Thiết lập xe đã hoàn thành nhiệm vụ về nhà xe
function Set_Busy_Car(busy, CARNO) {
    var data = {
        BUSY: busy,
        CARNO: CARNO
    };
    $.ajax({
        type: 'GET',
        url: '/update_busy/',
        data: data,
        success: function(response) {
            Alert_OK();
            $("#myDropdown_CAR_NUMCARD1").html('');
            response['returndata'].forEach(function Fill_Data(item, index) {
                $("#myDropdown_CAR_NUMCARD1").append(
                    '<a class="dropdown-item" href="#"  data-toggle="tooltip" data-placement="left" title="' + item['CAR_SIT'] + '(人) -' + item['DRIVER_NAME'] + '" data-original-title="' + item['CAR_SIT'] + ' (人) - ' + item['DRIVER_NAME'] + '" onclick="GET_CARDNO_INF(this)"><i class="fa fa-caret-right f-16 text-info" aria-hidden="true"></i>' + item['CARNO'] + '</a>'
                );
            });
            $("#Modal_biensoxe").modal('hide');
            $("#modal_xe").modal('hide');
            Search_Bus_Info();
        },
        error: function(response) { AlertErrorSQL(response); }
    });
}



$(document).ready(function() {

    //Cuộn Trở về đầu trang
    $(this).scrollTop(0);



    //Sự kiện tìm kiếm nhanh với ô tìm kiếm nhanh
    $("#search_docno_quick").keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {

            //Gọi Hàm tìm kiếm tên user 
            var docno = ($(event.target).val());
            var host = window.location.protocol + "//" + window.location.host;
            var hostname = window.location = host + "/archived/?docno=" + docno;
            window.location.assign(hostname);
            window.location = hostname;
            window.location.href = hostname;
            return false;
        }
    });



    //Sự kiện tìm kiếm nhanh với ô tìm kiếm nhanh
    $("#search_docno_quick2").keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {

            //Gọi Hàm tìm kiếm tên user 
            var docno = ($(event.target).val());
            var host = window.location.protocol + "//" + window.location.host;
            var hostname = window.location = host + "/archived/?docno=" + docno;
            window.location.assign(hostname);
            window.location = hostname;
            window.location.href = hostname;
            return false;
        }
    });



    //Sự kiện nhấn vào mục Hiển thị thông báo có đơn mới
    $("#notification_info").click(function() {
        SHOW_DOC_Notifications();
    });

    //Chọn ROW giữ trạng thái chọn trong bảng
    $('table').on('click', '.clickable-row', function(event) {
        $(this).addClass('table-warning').siblings().removeClass('table-warning');
    });



});