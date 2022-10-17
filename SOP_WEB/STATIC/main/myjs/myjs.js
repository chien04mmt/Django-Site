//Local variable
var FormName = '';

//Đường dẫn hình ảnh cho ảnh thẻ
var urlimg = '/static/main/Images/blank.JPG';
var urlimg2 = '/static/media/';

//Thông tin CSRFTOKEN
var csrf_name = '';
var csrf_value = '';

var mydate = new Date;

//Biến thực hiện hủy đơn thêm đơn hay phế đơn
var action_VB = '';
//Biến thực hiện gán funtion name vào button
var funtionName = '';
//Biến kiểm tra load html xong hay chưa
var loadhtm = 'N';




//Hỏi trước khi thực hiện trả về true-false:CONFIRM_Question()
//Hàm trả về biểu tượng của trạng thái đơn:SHOW_FLAG_STATUS(STATUS_DOC, size_icon)
//Hàm chỉ cho nhập vào số: ONLY_NUMBER_INPUT(element)
//Hàm chỉ cho input chữ hoa: UPERCASE_INPUT(element)
//lấy thông tin truyền hình ảnh vào formdata : GET_FORM_DATA_TO_POST(id_inputfile)
//TRuyền file trong thẻ input vào form: SET_FILE_TO_FORM_DATA_TO_POST(id_inputfile) 
//Lọc menu tìm kiếm DROPDOWN vơi input text: filterFunction(id_input, id_dropmenu)
//Lấy dữ liệu từ menu dropdownMenuButton truyền vào 1 input id: GET_TEXT_MENU(element, id_settext)
//Lấy toàn bộ ID và value của ID input đưa vào object: GET_ALL_INPUT_FROM_DIV(id_DIV)
//Lấy toàn bộ ID và value Checkbox được checked đưa vào object: GET_CHECKED_CHECKBOX_FROM_DIV(id_DIV)
//Click one input file: CLICK_InputFile(id_inputFile)
//Kiểm tra có tệp có phải là ảnh hay không: CHECK_IMAGE_FILE(element)
//Hàm kiểm tra dữ liệu từng đối tượng có null không: CHECK_ARR_NOT_NULL(arr)
//RESET trống thông tin của các thẻ con trong thẻ cha: RESET_AREA(id_area)
//Ẩn tất cả các button trong thẻ div: Hide_All_Button_FromDiv(id_DIV)
//Loại bỏ các thuộc tính hidden trong các thẻ button của thẻ DIV cha: Remove_Attr_Hidden_Button_FromDiv(id_DIV)
//Load lại trang: LOAD_PAGE_AGAIN()
//Kiểm tra trình duyệt có phải IE: CHECK_IE()
//Hiển thị Modal thông qua Show_Modal_FromID(id_modal)
//Đóng Modal thông qua ID: Close_Modal_FromID(id_modal)
//Checkbox thay đổi toàn bộ các checkbox khác:CHECKBOX_CHANGE_ALL(id_checkbox, id_Area)
//Show modal loadding: Show_loading()
//Countdown thoát Loading: Exit_Loading()
//Nhấn nút hủy bỏ: BACK_HOME()
// Hiển thị ảnh cá nhân: show_icon_user()
//Sự kiện enter cho 1 input thực hiện hàm fun:Enter_input(id_input, fun)
//Hiển thị thông tin chi tiết đơn vào form docdetail :Doc_Detail(el)
//Đi tới 1 liên kết( host + '/' + href_name + '/'): Goto_link(href_name)
//Đăng xuất tài khoản: LogOut()
//Tải file từ server về với 1 element: Donwload_File(element)
//Hàm tải file với tên file biết trước:downloadFile(fname)
//Tải file gộp với 1 file PDF khác:downloadFile_PDF_Merge(file1, file2, fname)
//Hàm lấy thông tin HOSTNAME: GET_HOSTNAME()
//Hàm trả về chuỗi thời gian dd-mm-yyy h:m: GET_STRING_DATETIME1(dateString)
//Hàm lấy thời gian hiện tại GET_TIME_NOW();
//Hàm trả về thông tin các đơn đang chờ ký: SHOW_DOC_Notifications()
//Hàm phân quyền cho các module: GET_perMission_module(idModule, val_fied)
//Hàm Phân quyền User các module: PERMISSION_USER()
//In chữ ký màu của thẻ Div: printDiv(divName)
//In chữ ký đen trắng của thẻ Div: PrintElem(elem)
//Cuộn Trở về đầu trang:    $(this).scrollTop(0);
//Load file HTML vào html: Load_html(id_DIV, path_html)
//Chuyển dữ liệu từ null hoặc undified về '':  ReMove_Null_String(obj)
//Load lại tooltip với datatable:   Reload_Datatable_(id_table)
//Xóa bảng và hủy phân trang của bảng:   Reset_Table_Datatable(id_table)
//Xóa row trong bảng delete_row(element) 
//Kiểm tra input chưa có dữ liệu: CHECK_FILL_DATA_INPUT(id_DIV)
//Phương thức ajax xử lý dữ liệu từ server : AJAX_REQUEST(url, type, data, func_OK)
//Tự động binding dữ liệu từ oject về các thẻ ID:  BINDING_DATA_TO_ID(oject)


//Chọn option trong select==> Add li vào Ul ID
function ChoiceOption_AddLi_Ul(element, id_ul) {
    $("#" + id_ul).append('<li class="select-multi select-choice" value="' + $(element).val() + '"><span>' + $("#" + element.id + " option:selected").text() + '</span> <i class="fa-del text-danger" onclick="$(this).parent().remove()">×</i></li>');
}


//Checkbox thay đổi giá trị khi tích chọn
function SetValue_CheckBox(element) {
    if ($(element).is(":checked")) { $(element).prop('value', '1') } else { $(element).prop('value', '0') }
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




//Kiểm tra báo vàng phần input chưa có dữ liệu
function CHECK_FILL_DATA_INPUT(id_DIV) {
    $("#" + id_DIV + " input").each(function() {
        if ($(this).val().length < 1) {
            $(this).css("background-color", "#f0e6e4")
                .attr("data-original-title", "Please fill this fiel.");
            $('#pass2id').removeAttr("style");
            return false;
        }
        return true;
    });
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



//Chuyển dữ liệu từ null hoặc undified về ''
function ReMove_Null_String(obj) {
    Object.keys(obj).forEach(function(key) {
        if (!obj[key]) { obj[key] = ''; }

        // console.log(key, obj[key]);
    });
    return obj;
}



//Load file HTML vào html:
function Load_html(id_DIV, path_html, action, functionButton) {
    $("#" + id_DIV).load(path_html, function() {
        action_VB = action;
        funtionName = functionButton;
        $("#btn_timkiem").attr('onclick', functionButton);
        loadhtm = 'Y';
        SHOW_LANG_();
        $("#btn_timkiem").click();
    });

}

//Load file HTML vào html:
function Load_html_1(id_DIV, path_html, functionButton) {
    $("#" + id_DIV).load(path_html, function() {
        $("#btn_timkiem").attr('onclick', functionButton);
        SHOW_LANG_();
    });

}


//Load file HTML vào html:
function Load_html_2(id_DIV, path_html, data_i18n, functionButton) {
    $("#" + id_DIV).load(path_html, function() {
        $("#title_a").attr('data-i18n', data_i18n);
        $("#btn_timkiem").attr('onclick', functionButton);
        SHOW_LANG_();
        $("#btn_timkiem").click();
    });

}




//Hỏi trước khi thực hiện
function CONFIRM_Question() {
    let text = "Are you sure ??";
    if (confirm(text) == true) {
        return true;
    } else {
        return false;
    }
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



//Hàm chỉ cho nhập vào số
function ONLY_NUMBER_INPUT(element) {
    $(element).keyup(function(e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value.replace(/\D/g, '');
        }
    });
}


//Hàm chuyển chữ Hoa input
function UPERCASE_INPUT(element) {
    $(element).val($(element).val().toUpperCase());
}


//lấy thông tin truyền hình ảnh vào formdata 
function GET_FORM_DATA_TO_POST(photo) {

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
    console.log(files.name);
    if (files.name.indexOf("+") > 0) {
        alert("Name file error '+'");
        e.preventDefault();
    }
    formData.append('myfile', files);
    formData.append('file_length', 1);
    return formData;
}



//TRuyền file trong thẻ input vào form
function SET_FILE_TO_FORM_DATA_TO_POST(id_inputfile) {

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

    var files = $('#id_inputfile')[0].files[0];
    // console.log(files.name);
    if (files.name.indexOf("+") > 0) {
        alert("Name file error '+'");
        e.preventDefault();
    }
    formData.append('myfile', files);
    formData.append('file_length', 1);
    return formData;
}

//Upfile lên server
function UPLOAD_FILE_TO_SERVER(id_File_input, fun) {
    var photo = $('#' + id_File_input)[0].files[0];
    formData = GET_FORM_DATA_TO_POST(photo);
    $.ajax({
        type: "POST",
        data: formData,
        url: "/simple_upload/",
        contentType: false,
        processData: false,
        headers: { "X-CSRF-Token": csrf_value },
        success: function(response) {
            // Alert_OK();
            // console.log(response['returndata'][0]);
            fun(response['returndata'][0]);
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
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



//Lấy toàn bộ ID và value Checkbox được checked đưa vào object
function GET_CHECKED_CHECKBOX_FROM_DIV(id_DIV) {
    var data = {}
    $("#" + id_DIV + " :input").each(function() {
        if ($(this).is(":checked")) {
            data[$(this).attr('id')] = $(this).attr('id');
        }
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




//Click one input file
function CLICK_InputFile(id_inputFile) {
    $("#" + id_inputFile).click();
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





//Hàm kiểm tra dữ liệu từng đối tượng có null không
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



//Load lại trang
function LOAD_PAGE_AGAIN() {
    //location.reload();
    window.location.href = window.location.href;
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
                    .prop('src', '/static/main/img/pen.jpg' + "?" + d.getTime());

                $("#img_profile")
                    .removeAttr('src')
                    .prop('src', '/static/main/img/pen.jpg' + "?" + d.getTime());

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


//Sự kiện enter cho 1 input thực hiện hàm fun:
function Enter_input(id_input, fun) {
    $("#" + id_input).keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {
            fun();
        }
    });
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




//Truyền 1 biến của element vào href(GET) :
function Goto_href_variable(el, href) {
    var docno = $(el).text();
    var variable_name = $(el).attr('id');
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/' + href + '/?' + variable_name + "=" + docno
    window.open(newhref, '_blank'); //Mở 1 tab mới
    // window.open(newhref);
    // window.location = newhref;
}


//Mở 1 tab liên kết( host + '/' + href_name + '/'):
function Open_link(href_name, Optional) {
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/' + href_name
    window.open(newhref, Optional); //Mở 1 tab mới _blank(đi tới _self)
}



//Đi tới 1 liên kết( host + '/' + href_name + '/'):
function Goto_link(href_name) {
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/' + href_name + '/'
    window.location = newhref;
}



//Đi tới 1 liên kết( host + '/' + href_name + '/'):
function Goto_link_data(href_name, data) {
    var host = window.location.protocol + "//" + window.location.host;
    var newhref = host + '/' + href_name + '/?' + data
    window.location = newhref;
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



//Tải file từ server về với 1 element
function Donwload_File(element) {
    var filename = $(element).text();
    // alert('msg');
    downloadFile(filename);
}



//Hàm tải file với tên file biết trước
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



//Tải file gộp với 1 file PDF khác
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
    today = dd + "/" + mm + "/" + y + " " + h + ":" + m + " " + ampm;
    return today;
}

//Lấy thời gian hiện tạ: yyyy/mm/dd hh:mmss AM
function GET_TIME_NOW() {
    return new Date().toString();
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
                            <img class="d-flex align-self-center img-radius" src="/static/main/img/pen.jpg" alt="User image">\
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
                        <img class="d-flex align-self-center img-radius" src="/static/main/media/' + img + '" alt="User image">\
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
    function func(response) {

        var item = response["returndata"];
        // console.log(item);
        item.forEach(function FILL_DATA(ite, index) {
            GET_perMission_module(ite['Code']);
        });
    }
    AJAX_REQUEST_RESPONSE('/show_permission/', 'GET', '', func);
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

//Di chuyển modal :
function Move_modal(id_modalDialog) {
    $("#" + id_modalDialog).draggable();
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


});




//Tự động binding dữ liệu từ oject về các thẻ ID
function BINDING_DATA_TO_ID(oject) {
    // for (var [key, value] of Object.entries(oject)) {
    //     $("#" + key).val(value);
    // }

    $.each(oject, function(key, value) {
        $("#" + key).val(value);
    });

}