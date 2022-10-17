//Set cookie CRSTOCKEN

function Set_cookie_CRSTOKEN() {
    var csrfmiddlewaretoken = 'csrftoken';
    var value = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    //var value = $("input[name=csrfmiddlewaretoken]").val();
    setCookiex(csrfmiddlewaretoken, value);
}

function setCookiex(key, value, day) {
    var expires = new Date();
    expires.setTime(expires.getTime() + day * 24 * 60 * 60 * 1000); //1 hour
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString() + "; path=/";
}


function getCookiexUser() {
    const value = ';' + document.cookie;
    const parts = value.split(';');
    for (i = 0; i <= parts.length; i++) {
        textuser = (parts[i]);
        try {
            if (textuser.lastIndexOf('=PKs') > 0) {
                user = textuser.substring(5, textuser.lastIndexOf("=PKs||"));
                pass = textuser.substring(textuser.lastIndexOf("PKs||") + 5);
                // alert(user);
                // alert(Base64.decode(user));
                // alert(Base64.decode(pass));
                $("#myDropdown_USER").append('<a id="' + pass + '" class="dropdown-item" href="#"  data-toggle="tooltip" data-placement="left" title="Pass:' + pass + '" data-original-title="Pass:' + pass + '" onclick="GET_User_Show(this)"><i class=" fa fa-user-circle text-info" aria-hidden="true"> &ensp;</i>' + Base64.decode(user) + '</a>');
            }
        } catch {}

    }
}




//tự động chọn user
function GET_User_Show(element) {
    // console.log(element);
    $("#username").val($(element).text().replaceAll("\\s\\s+", " ").trim());
    $("#pass1id").val(Base64.decode($(element).attr('id')));
    $("#input_captcha").focus();
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


$(document).ready(function() {
    getCookiexUser("USer_");
});