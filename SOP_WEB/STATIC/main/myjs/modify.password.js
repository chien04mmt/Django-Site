//check valid element input
function isValid(el) {
    var regex = /[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ]/i // regex here
    var valid = regex.test(el.val());
    if (!valid) {
        // Check if popover is already visible to handle flicker effect.
        if (el.val().length == 0) {
            el.popover({
                placement: 'top',
            }).popover('show');
            return false;
        } else {
            el.popover('hide');
            return true;
        }
    }
}




//Check 2 Password
function isValid_password(el1, el2) {
    if (el1.val() != el2.val()) {
        // Check if popover is already visible to handle flicker effect.
        el1.popover({
            placement: 'top',
            content: 'The password is not the same!'
        }).popover('show');
        return false;
    } else {
        el1.popover('hide');
        return true;
    }
}




//Kiểm tra ký tự nhập vào ô Application title
function isValid1(str) {
    var re = /[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ]/i // regex here
    if (re.test(str)) {
        alert("ERROR IN PUT DATA FORMAT! " + "<" + str + ">");
        return false;
    } else {
        return true;
    }
}



//Modifiels Password trên modal
function Save_ModifielsPassword() {
    var data = {
        userID: $("#userid_modal").val(),
        DFSite: $("#siteid_modal option:selected").text(),
        division: $("#buid_modal option:selected").text(),
        UserName: $("#usernameid_modal").val(),
        Emp_NO: $("#empnoid_modal").val(),
        Dept: $("#deptid_modal").val(),
        CostNo: $("#costnoid_modal").val(),
        Telephone: $("#extid_modal").val(),
        mailbox: $("#emailid_modal").val(),
        Password1: $("#pass1id_modal").val(),
        Password2: $("#pass2id_modal").val()
    };

    $.ajax({
        type: 'GET',
        url: "/saveprofile/",
        data: data,
        //contentType: "application/json; charset=utf-8",
        //traditional: true,

        success: function(response) {
            Alert_OK();
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}




//Lưu  thông tin người dùng trên modal
function Save_profiles_form() {
    if (CHECK_FILL_DATA_INPUT('div_profile') == false) { return };
    if (isValid($("#pass1id")) == false) { return; }
    if (isValid($("#pass2id")) == false) { return; }
    if (isValid_password($("#pass1id"), $("#pass2id")) == false) { Show_Alert_Message("Mật khẩu không khớp! (密碼錯誤)"); return; }
    if (CHECK_IE()) {
        if (CONFIRM_Question()) {
            Save_ModifielsPassword_form();
        }
    } else {
        Swal.fire({
            title: 'Are you sure?',
            text: "You are changing your information profile!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, Change it!'
        }).then(function(result) {
            if (result.isConfirmed) {
                Save_ModifielsPassword_form();
            }
        })
    }

}




//Lưu Modifiels Password trên Form
function Save_ModifielsPassword_form() {

    var data = {
        userID: $("#userid").val().toUpperCase(),
        DFSite: $("#siteid option:selected").text(),
        division: $("#buid").val(),
        UserName: $("#usernameid").val(),
        Emp_NO: $("#empnoid").val().toUpperCase(),
        Dept: $("#deptid").val(),
        CostNo: $("#costnoid").val().toUpperCase(),
        Telephone: $("#extid").val(),
        mailbox: $("#emailid").val(),
        Password1: $("#pass1id").val(),
        Password2: $("#pass2id").val()
    };
    $.ajax({
        type: 'GET',
        url: "/saveprofile/",
        data: data,
        success: function(response) {
            Alert_OK();
            SHOW_DOC_Notifications();
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//Hiển thị Modifiels Password trên FORM
function ShowModifyProfile_form() {
    $.ajax({
        type: 'GET',
        url: "/showprofile/",
        data: { "data": 'show_profile' },
        success: function(response) {
            var str = JSON.stringify(response['returndata']);
            var arrdic = JSON.parse(str);
            var fields = arrdic[0];
            var pass = arrdic[1];

            $("#userid").val(fields.UserID).toUpperCase();
            $("#usernameid").val(fields.UserName).toUpperCase();
            $("#empnoid").val(fields.Emp_NO).toUpperCase();
            $("#deptid").val(fields.Dept).toUpperCase();
            $("#costnoid").val(fields.CostNo).toUpperCase();
            $("#extid").val(fields.Telephone);
            $("#emailid").val(fields.mailbox);
            $("#pass1id").val();
            $("#pass2id").val();
            $('#buid').val(fields.division);
            // var newOption1 = new Option(fields.division, '', false, false);
            // $('#buid').append(newOption1).trigger('change');
            var newOption2 = new Option(fields.DFSite, '', false, false);
            $('#siteid').append(newOption2).trigger('change');
            $("#pass1id").val(response['pass']);

        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}




var x = document.getElementById("pass1id");
var z = document.getElementById("pass2id");
var y = document.getElementById("togglePassword")

//Show and Hide password 
function SHOW_PASSWORD() {
    if (x.type === "password") {
        x.type = "text";
        z.type = "text";
        y.classList.remove("fa-eye-slash");
        y.classList.add("fa-eye");
    } else {
        x.type = "password";
        z.type = "password";
        y.classList.remove("fa-eye");
        y.classList.add("fa-eye-slash");
    }
}




//Nhấn nút change Images
function CHANGE_AVATAR(element, id_img) {
    var photo = $(element)[0].files[0];
    // alert(photo.name);
    if (CHECK_IMAGE_FILE(element) == false) {
        preventDefault();
    }
    Upload_AVATAR(photo, id_img)
}

function Upload_AVATAR(photo, id_img) {
    var formData = GET_FORM_DATA_TO_POST(photo);

    //Gửi dữ liệu file lên server trong myfile
    $.ajax({
        type: "POST",
        data: formData,
        url: "/change_image/",
        contentType: false,
        processData: false,
        headers: { "X-CSRF-Token": csrf_value },
        success: function(response) {
            var img = response['returndata']['filename'];
            // alert(id_img);
            d = new Date();
            $("#" + id_img).removeAttr('src');
            $("#" + id_img).prop('src', urlimg2 + img + "?" + d.getTime());

            $("#img_avatar").removeAttr('src')
                .removeAttr('src')
                .prop('src', urlimg2 + img + "?" + d.getTime());
            Alert_OK();
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });

}


//LOAD Thông tin quyền người đăng nhập
function LOAD_PERMISSION_USER() {
    $.ajax({
        type: 'GET',
        url: "/showpermission_me/",
        data: 'data',
        success: function(response) {
            var rep = response['returndata'][0]
            if (rep.APPROVAL == 1) { $("#chk_APPROVAL").prop('checked', true); }
            if (rep.NEW_APP_CREAT == 1) { $("#chk_NEW_APP_CREAT").prop('checked', true); }
            if (rep.QUERY_DOC == 1) { $("#chk_QUERY_DOC").prop('checked', true); }
            if (rep.API_CREATE_USER == 1) { $("#chk_CREATE_user").prop('checked', true); }
            if (rep.FLOW_SET == 1) { $("#chk_FLOW_SET").prop('checked', true); }
            if (rep.FORM_SET == 1) { $("#chk_FORM_SET").prop('checked', true); }
            if (rep.APPROVER_SET == 1) { $("#chk_APPROVER_SET").prop('checked', true); }
            if (rep.USER_MANAGE == 1) { $("#chk_USER_MANAGE").prop('checked', true); }
            if (rep.PASS_MODIFY == 1) { $("#chk_PASS_MODIFY").prop('checked', true); }
            $("#modalpermission_self").modal('show');
            //Gọi hàm hiển thị quyền
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}


$(document).ready(function() {
    $("#div_profile input").click(function() {
        $(this)
            .removeAttr("data-original-title")
            .popover('hide');
    });

});