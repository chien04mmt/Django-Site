// Create Base64 Object
var Base64 = {
    _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    encode: function(e) {
        var t = "";
        var n, r, i, s, o, u, a;
        var f = 0;
        e = Base64._utf8_encode(e);
        while (f < e.length) {
            n = e.charCodeAt(f++);
            r = e.charCodeAt(f++);
            i = e.charCodeAt(f++);
            s = n >> 2;
            o = (n & 3) << 4 | r >> 4;
            u = (r & 15) << 2 | i >> 6;
            a = i & 63;
            if (isNaN(r)) { u = a = 64 } else if (isNaN(i)) { a = 64 }
            t = t + this._keyStr.charAt(s) + this._keyStr.charAt(o) + this._keyStr.charAt(u) + this._keyStr.charAt(a)
        }
        return t
    },
    decode: function(e) {
        var t = "";
        var n, r, i;
        var s, o, u, a;
        var f = 0;
        e = e.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (f < e.length) {
            s = this._keyStr.indexOf(e.charAt(f++));
            o = this._keyStr.indexOf(e.charAt(f++));
            u = this._keyStr.indexOf(e.charAt(f++));
            a = this._keyStr.indexOf(e.charAt(f++));
            n = s << 2 | o >> 4;
            r = (o & 15) << 4 | u >> 2;
            i = (u & 3) << 6 | a;
            t = t + String.fromCharCode(n);
            if (u != 64) { t = t + String.fromCharCode(r) }
            if (a != 64) { t = t + String.fromCharCode(i) }
        }
        t = Base64._utf8_decode(t);
        return t
    },
    _utf8_encode: function(e) {
        e = e.replace(/\r\n/g, "\n");
        var t = "";
        for (var n = 0; n < e.length; n++) {
            var r = e.charCodeAt(n);
            if (r < 128) { t += String.fromCharCode(r) } else if (r > 127 && r < 2048) {
                t += String.fromCharCode(r >> 6 | 192);
                t += String.fromCharCode(r & 63 | 128)
            } else {
                t += String.fromCharCode(r >> 12 | 224);
                t += String.fromCharCode(r >> 6 & 63 | 128);
                t += String.fromCharCode(r & 63 | 128)
            }
        }
        return t
    },
    _utf8_decode: function(e) {
        var t = "";
        var n = 0;
        var r = c1 = c2 = 0;
        while (n < e.length) {
            r = e.charCodeAt(n);
            if (r < 128) {
                t += String.fromCharCode(r);
                n++
            } else if (r > 191 && r < 224) {
                c2 = e.charCodeAt(n + 1);
                t += String.fromCharCode((r & 31) << 6 | c2 & 63);
                n += 2
            } else {
                c2 = e.charCodeAt(n + 1);
                c3 = e.charCodeAt(n + 2);
                t += String.fromCharCode((r & 15) << 12 | (c2 & 63) << 6 | c3 & 63);
                n += 3
            }
        }
        return t
    }
}

// // Define the string
// var string = 'Hello World!';

// // Encode the String
// var encodedString = Base64.encode(string);
// console.log(encodedString); // Outputs: "SGVsbG8gV29ybGQh"

// // Decode the String
// var decodedString = Base64.decode(encodedString);
// console.log(decodedString); // Outputs: "Hello World!"




//Ajax LOG_OUT
function LogOut() {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/logout/",
        data: { "data": 'logout' },
        success: function(response) {},
        error: function(response) {
            // alert the error if any error occured
            AlertErrorSQL(response);
        }
    })
}

//Login FORM
var result = "";

function myFunction() {
    makeid(5);
};

function makeid(length) {
    result = "";
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    };
    var div_input_1 = document.getElementById("kq_input_1");
    if (result.length <= 1) { result = "3JC0O"; }
    div_input_1.innerHTML = result;
};

function check_captcha() {
    var a = $('#input_captcha').val();
    if (a == result) {
        if ($("#rememberpass").is(":checked")) {
            setCookiex('USer_' + Base64.encode(document.getElementById('username').value), "PKs||" + Base64.encode(document.getElementById('pass1id').value), 365);
        }
        return true;
    } else {
        preventDefault();
        alert("Error Input Captcha Text !");
    }
}





//Forgot password FORM
function validatEmail() {
    var x = document.myform.email.value;
    var atposition = x.indexOf("@");
    var dotposition = x.lastIndexOf(".");
    if (atposition < 1 || dotposition < (atposition + 2) ||
        (dotposition + 2) >= x.length) {
        alert("Please enter a valid e-mail address.");
        preventDefault();
        return false;
    } else {
        //alert("OK ! your password sent to your email ! Please check mailbox!");							
        return true;
    }
}

//Check pass FORM Register Acount Esign
function check_password() {
    var a = $('#pass1').val();
    var b = $('#pass2').val();
    if (a == b) {
        return true;
    } else {
        alert("Passwords are not the same!");
        preventDefault();
    }
}



var x = document.getElementById("pass1id");
var y = document.getElementById("togglePassword");
//Show and Hide password 
function SHOW_PASSWORD() {
    if (x.type === "password") {
        x.type = "text";
        y.className = "fad fa-eye";
    } else {
        x.type = "password";
        y.className = "fad fa-eye-slash";
    }
}

$(document).ready(function() {
    $(y).mousedown(function() {
        SHOW_PASSWORD();
    })
})