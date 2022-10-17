const urlstatic_JS = $("#urlstatic_JS").text();
var langcode = 'en';

// "use strict"
// class Translator {
//     constructor() {
//         this._lang = 'cn';
//         this._elements = document.querySelectorAll("[data-i18n]");
//     }


//     translate(translation) {
//         this._elements.forEach(function(element) {
//             var keys = element.dataset.i18n.split(".");
//             var text = keys.reduce(function(obj, i) { return obj[i] }, translation);
//             if (text) {
//                 element.innerHTML = text;
//             }
//         });
//     }

//     Translation() {
//         fetch(this._lang + '.json')
//             .then(function(response) {
//                 this.translate(response);
//             })

//         .then(function(translation) {
//                 console.log('Request successful', text);
//             })
//             .catch(function(error) {
//                 log('Can not load lang file', error)
//             });
//     }

// }


//set language cookie
function setcookie_lang(lang, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = 'lang_esign4.0=' + lang + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
//Get langcookie
function getcookie_lang() {
    var lang = getCookie("lang_esign4.0");
    if (lang) { return getCookie("lang_esign4.0"); } else { setcookie_lang('en', 365); return 'en'; }

}

$(document).ready(function() {

    //Sự kiện nhấn vào chọn ngôn ngữ
    $(".dropdown-item").click(function() {
        var lang = $(this).text();
        if (lang.indexOf('Việt') > 0) {
            lang = 'vn';
            $("#img_lang")
                .removeAttr('src')
                .prop('src', urlstatic_JS + 'images/vn.png');
            $("#txt_lang").text("Vietnamese");
            Change_Lang(lang);
            setcookie_lang(lang, 365);
            SHOW_LANG_();
        };
        if (lang.indexOf('English') > 0) {
            lang = 'en';
            $("#img_lang")
                .removeAttr('src')
                .prop('src', urlstatic_JS + 'images/en.png');
            $("#txt_lang").text("English");
            Change_Lang(lang);
            setcookie_lang(lang, 365);
            SHOW_LANG_();
        };
        if (lang.indexOf('中文') > 0) {
            lang = 'cn';
            $("#img_lang")
                .removeAttr('src')
                .prop('src', urlstatic_JS + 'images/cn.jpg');
            $("#txt_lang").text("中文");
            Change_Lang(lang);
            setcookie_lang(lang, 365);
            SHOW_LANG_();
        };

    });

});



//Lấy thông tin trên ngữ trên server
function GET_LANG() {
    function func(response) {
        try {
            var langcode = response["returndata"];
            if (langcode == 'en' || langcode == 'vn' || langcode == 'cn') {
                setcookie_lang(langcode, 365);
            } else {
                setcookie_lang('vn', 365);
            }

        } catch (err) {
            setcookie_lang('vn', 365);
        }
        // alert(langcode);
        SHOW_LANG_();
    }
    AJAX_REQUEST_RESPONSE('/get_lang/', 'GET', 'data', func);

}



//Thay đổi thông tin ngôn ngữ trên DB
function Change_Lang(lang) {
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "/change_lang/",
        data: {
            lang: lang
        },
        success: function(response) {
            GET_LANG();
        },
    })
}

//set logo language for buton
function set_Icon_langbutton(lang) {
    if (lang == 'vn') {
        $("#img_lang")
            .removeAttr('src')
            .prop('src', urlstatic_JS + 'images/vn.png');
        $("#txt_lang").text(' Việt Nam');
    }

    if (lang == 'cn') {
        $("#img_lang")
            .removeAttr('src')
            .prop('src', urlstatic_JS + 'images/cn.jpg');
        $("#txt_lang").text(' 中文');
    }
    if (lang == 'en') {
        $("#img_lang")
            .removeAttr('src')
            .prop('src', urlstatic_JS + 'images/en.png');
        $("#txt_lang").text(' English');
    }
}
//
function SHOW_LANG_() {
    var lang = getcookie_lang();
    set_Icon_langbutton(lang);

    var jsonUrl = urlstatic_JS + "lang/i18n/" + lang + ".json";

    _elements = document.querySelectorAll("[data-i18n]");

    function translate(translation) {
        Array.prototype.slice.call(_elements, 0).forEach(function(element) {
            var keys = element.dataset.i18n.split(".");
            var text = keys.reduce(function(obj, i) { return obj[i] }, translation);
            if (text) {
                element.innerHTML = text;
                $(element)
                    .removeAttr('placeholder')
                    .prop('placeholder', text);
            }
        });

    }

    $.ajax({
        url: jsonUrl,
        dataType: "json",
        async: false,
        success: translate
    });
}