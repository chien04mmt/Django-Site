//check valid element input
function isValid(el) {
    var regex = /[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ]/i // regex here
    var valid = regex.test(el.val());
    if (!valid) {
        // Check if popover is already visible to handle flicker effect.
        if (el.val().length == 0) {
            el.popover({
                placement: 'right',
                content: 'This is not a valid'
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
            placement: 'right',
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




// //Chỉnh sửa thông tin người dùng trên modal
// function Save_profiles() {
//     // if (isValid($("#pass1id")) == false) { return; }
//     // if (isValid($("#pass2id")) == false) { return; }
//     // if (isValid_password($("#pass1id"), $("#pass2id")) == false) { return; }

//     Swal.fire({
//         title: 'Are you sure?',
//         text: "You are changing your information profile!",
//         icon: 'warning',
//         showCancelButton: true,
//         confirmButtonColor: '#3085d6',
//         cancelButtonColor: '#d33',
//         confirmButtonText: 'Yes, Change it!'
//     }).then((result) => {
//         if (result.isConfirmed) {
//             Save_ModifielsPassword();
//             Swal.fire(
//                 'Saved!',
//                 'Your file has been saved.',
//                 'success'
//             )
//             ShowModifyProfile();
//         }
//     })
// }

//Modifiels Password trên modal
function Save_ModifielsPassword() {
    var userID = $("#userid_modal").val();
    var UserName = $("#usernameid_modal").val();
    var Emp_NO = $("#empnoid_modal").val();
    var Dept = $("#deptid_modal").val();
    var CostNo = $("#costnoid_modal").val();
    var Telephone = $("#extid_modal").val();
    var mailbox = $("#emailid_modal").val();
    var Password1 = $("#pass1id_modal").val();
    var Password2 = $("#pass2id_modal").val(); // Get value text box

    var DFSite = $("#siteid_modal option:selected").text(); //Get value Select box
    var division = $("#buid_modal option:selected").text();

    var data = {
        userID: userID,
        DFSite: DFSite,
        division: division,
        UserName: UserName,
        Emp_NO: Emp_NO,
        Dept: Dept,
        CostNo: CostNo,
        Telephone: Telephone,
        mailbox: mailbox,
        Password1: Password1,
        Password2: Password2
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




// //Hiển thị Modifiels Password trên FORM
// function ShowModifyProfile() {
//     $.ajax({
//         type: 'GET',
//         url: "/showprofile/",
//         data: { "data": 'show_profile' },
//         success: function(response) {
//             var str = JSON.stringify(response['returndata']);
//             var arrdic = JSON.parse(str);
//             var fields = arrdic[0];
//             $("#userid_modal").val(fields.UserID);
//             $("#usernameid_modal").val(fields.UserName);
//             $("#empnoid_modal").val(fields.Emp_NO);
//             $("#deptid_modal").val(fields.Dept);
//             $("#costnoid_modal").val(fields.CostNo);
//             $("#extid_modal").val(fields.Telephone);
//             $("#emailid_modal").val(fields.mailbox);
//             $("#pass1id_modal").val();
//             $("#pass2id_modal").val();
//             var newOption1 = new Option(fields.division, '', false, false);
//             $('#buid_modal').append(newOption1).trigger('change');
//             var newOption2 = new Option(fields.DFSite, '', false, false);
//             $('#siteid_modal').append(newOption2).trigger('change');
//             $("#pass1id_modal").val(fields.PassWord);

//         },
//         error: function(response) {
//             AlertErrorSQL(response);
//         }
//     })
//     $('#exampleModal').modal('show');
// }

//Lưu  thông tin người dùng trên modal
function Save_profiles_form() {
    // if (isValid($("#pass1id")) == false) { return; }
    // if (isValid($("#pass2id")) == false) { return; }
    if (isValid_password($("#pass1id"), $("#pass2id")) == false) { alert("Check Password again!"); return; }
    if (CHECK_IE()) {
        if (CONFIRM_Question()) {
            Save_ModifielsPassword_form();
            ShowModifyProfile_form();
            $("#Modal_Add_Acount").modal('hide');
            SHOW_INPUT_PASS();
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
                ShowModifyProfile_form();
                $("#Modal_Add_Acount").modal('hide');
                SHOW_INPUT_PASS();
            }
        })
    }

}




//Lưu Modifiels Password trên Form
function Save_ModifielsPassword_form() {
    var userID = $("#userid").val().toUpperCase();
    var UserName = $("#usernameid").val().toUpperCase();
    var Emp_NO = $("#empnoid").val().toUpperCase();
    var Dept = $("#deptid").val().toUpperCase();
    var CostNo = $("#costnoid").val().toUpperCase();
    var Telephone = $("#extid").val();
    var mailbox = $("#emailid").val();
    var Password1 = $("#pass1id").val();
    var Password2 = $("#pass2id").val(); // Get value text box

    var DFSite = $("#siteid option:selected").text(); //Get value Select box
    var division = $("#buid option:selected").text();

    var data = {
        userID: userID,
        DFSite: DFSite,
        division: division,
        UserName: UserName,
        Emp_NO: Emp_NO,
        Dept: Dept,
        CostNo: CostNo,
        Telephone: Telephone,
        mailbox: mailbox,
        Password1: Password1,
        Password2: Password2
    };
    $.ajax({
        type: 'GET',
        url: "/saveprofile/",
        data: data,
        success: function(response) {
            Alert_OK();
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
            var newOption1 = new Option(fields.division, '', false, false);
            $('#buid').append(newOption1).trigger('change');
            var newOption2 = new Option(fields.DFSite, '', false, false);
            $('#siteid').append(newOption2).trigger('change');
            $("#pass1id").val(response['pass']);

        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    })
}



//Show and Hide password 
function SHOW_PASSWORD() {

    var x = document.getElementById("pass1id");
    var z = document.getElementById("pass2id");
    var y = document.getElementById("togglePassword")
    if (x.type === "password") {
        x.type = "text";
        z.type = "text";
        y.className = "fas fa-eye-slash";
    } else {
        x.type = "password";
        z.type = "password";
        y.className = "fas fa-eye";
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
            // Alert_OK();
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });

}












// function thisFileUpload(element) {
//     var id = $(element).attr('id');
//     document.getElementById(id).click();
// }






// //Thay đổi ảnh nền cá nhân
// try {
//     document.getElementById('file_user').onchange = uploadOnChange2;
// } catch (error) {
//     alert('Not change Avartar');
// }





// //Upload file FORM lên server
// function Upload_file_IMG() {

//     //Check input file
//     if ($("#file_user").val().length == 0) {
//         Swal.fire('Please Choose Files Application...!', '', 'warning')
//         e.preventDefault();
//     }
//     var csrf_name = '';
//     var csrf_value = '';
//     // Sử dụng jquery:
//     var formData = new FormData($('#frm_formfile')[0]);
//     //Lấy mã csrftocken gán vào Formdata
//     $("#frm_csftk").each(function() {
//         if ($(this).find(':input')) {
//             btn = $(this).find(':input');
//             csrf_name = $(btn).attr('name');
//             csrf_value = $(btn).attr('value');
//             formData.append(csrf_name, csrf_value);
//         }
//     });

//     var files = $('#file_user')[0].files;
//     var res = Array.prototype.slice.call(files);
//     for (var i = 0; i < files.length; i++) {
//         if (files[i].name.indexOf("+") > 0) {
//             alert("Name file error '+'");
//             e.preventDefault();
//         }
//         formData.append('myfile' + i, files[i]);
//     }
//     formData.append('file_length', files.length);
//     //Gửi dữ liệu file lên server trong myfile

//     $.ajax({
//         type: "POST",
//         data: formData,
//         url: "/change_image/",
//         contentType: false,
//         processData: false,
//         headers: { "X-CSRF-Token": csrf_value },
//         success: function(response) {
//             var img = response['returndata'];
//             $("#bg_user img").remove('img');
//             $("#bg_user").append('<img src="' + urlstatic_JS + "media/" + img + '">');
//         },
//         error: function(data) {
//             AlertErrorSQL(data);
//         }
//     });

// }



// function uploadOnChange2() {

//     try {
//         filex = $('#file_user')[0].files;
//     } catch (error) {
//         event.defaultPrevented();
//     }

//     var validImageTypes = ['image/gif', 'image/jpeg', 'image/png', 'image/bmp'];
//     for (var i = 0; i < filex.length; i++) {
//         var fileType = filex[i]['type'];
//         if (!validImageTypes.includes(fileType)) {
//             alert("Not Image File, check again!");
//             event.defaultPrevented();
//         }
//         Upload_file_IMG();
//         // Update_Image_profile(filex[i].name);
//     }
//     window.location.reload();
// }



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