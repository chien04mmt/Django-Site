//Thông báo OK
function Alert_OK() {
    window.showAlert = function() {
            alertify.alert('<div class="text-info">Action OK</div>');
        }
        //works with modeless too
    alertify.alert().setting('modal', true);
    window.showAlert();
    $('.ajs-header').text('Notice !');
}



//THông báo Nhập các trường dữ liệu
function Alert_Fill_data() {
    window.showAlert = function() {
            alertify.alert('<div class="text-danger">Please fill all fields..</div>');
        }
        //works with modeless too
    alertify.alert().setting('modal', true);
    window.showAlert();
    $('.ajs-header').text('Notice !');
    event.preventDefault();
}



//Thông báo NG sweatAlert2
function AlertErrorSQL(response) {
    var text = response['responseJSON'];
    text = JSON.stringify(text);
    alert('<div class="text-danger">' + text + '</div>');
    defaultPrevented();
}




//Hỏi thực hiện hàm trong IE
function CONFIRM_ALERT(title, text, text_btnOK, text_btnCancel, func) {
    var pre = document.createElement('pre');
    //custom style.
    pre.style.maxHeight = "400px";
    pre.style.margin = "0";
    pre.style.padding = "24px";
    pre.style.whiteSpace = "pre-wrap";
    pre.style.textAlign = "justify";
    pre.appendChild(document.createTextNode(text));
    $('.ajs-header').text(title);
    //show as confirm
    alertify.confirm(pre, function() {
        func();
        alertify.success(text_btnOK);
    }, function() {
        alertify.error(text_btnCancel);
    }).set({ labels: { ok: text_btnOK, cancel: text_btnCancel }, padding: false });

}



//Hỏi thực hiện hàm trong IE với func và param
function CONFIRM_ALERT_Param(title, text, text_btnOK, text_btnCancel, func, param) {
    var pre = document.createElement('pre');
    //custom style.
    pre.style.maxHeight = "400px";
    pre.style.margin = "0";
    pre.style.padding = "24px";
    pre.style.whiteSpace = "pre-wrap";
    pre.style.textAlign = "justify";
    pre.appendChild(document.createTextNode(text));
    $('.ajs-header').text(title);
    //show as confirm
    alertify.confirm(pre, function() {
        func(param);
        alertify.success(text_btnOK);
    }, function() {
        alertify.error(text_btnCancel);
    }).set({ labels: { ok: text_btnOK, cancel: text_btnCancel }, padding: false });


}


//Hiên thị thông tin truyền vào
function Show_Alert(title, text_btOk, message) {
    var pre = document.createElement('pre');
    //custom style.
    pre.style.maxHeight = "400px";
    pre.style.margin = "0";
    pre.style.padding = "24px";
    pre.style.whiteSpace = "pre-wrap";
    pre.style.textAlign = "justify";
    pre.appendChild(document.createTextNode(message));
    $('.ajs-header').text(title);
    //show as confirm
    alertify.confirm(pre, function() {
        func(param);
        alertify.success(text_btnOK);
    }).set({ labels: { ok: text_btOk }, padding: false });

}