//Question confirm with param
function CONFIRM_ALERT_Param(title, text, text_btnOK, text_btnCancel, fun, param) {
    Swal.fire({
        title: title,
        text: text,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#FF7043',
        // cancelButtonColor: '#d33',
        confirmButtonText: text_btnOK,
        cancelButtonText: text_btnCancel,

    }).then((result) => {
        if (result.isConfirmed) {
            fun(param);
        }
    })
}


//Question confirm with param
function CONFIRM_ALERT(title, text, text_btnOK, text_btnCancel, fun, param) {
    Swal.fire({
        title: title,
        text: text,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#FF7043',
        // cancelButtonColor: '#d33',
        confirmButtonText: text_btnOK,
        cancelButtonText: text_btnCancel,

    }).then((result) => {
        if (result.isConfirmed) {
            fun(param);
        }
    })
}

//Thông báo NG sweatAlert2
function AlertErrorSQL(response) {
    var text = response['responseJSON'];
    text = JSON.stringify(text);
    // clearInterval(yourInterval);
    Swal.fire({
        title: '通報 / Thông báo',
        text: text,
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Retry!'
    }).then(function(result) {

        if (result.isConfirmed) {
            // setInterval1();
        }
    })

}


//THông báo OK sweatAlert2
function Alert_OK() {
    Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
    })

}


//THông báo Nhập các trường dữ liệu
function Alert_Fill_data() {
    Swal.fire({
        title: 'Thông báo!(警報)',
        text: 'Vui lòng điền đủ thông tin..(請填寫所有字段)',
        imageUrl: "../static/img/pen.jpg",
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })

}




//THông báo hỏi lại sweatAlert2 với ajax OK
function Remind_Question_Ajax(url, type, data, func_ajax, fun_success_ajax) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Bạn chắc chắn?(你確定嗎)',
        text: "Bạn không thể hoàn nguyên việc này! (您將無法還原此內容！)",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Có (是的)',
        cancelButtonText: 'Hủy/取消',
        reverseButtons: true
    }).then(function(result) {
        if (result.isConfirmed) {
            func_ajax(url, type, data, fun_success_ajax);
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            return false;
        }
    })
    return true;
}


//THông báo hỏi lại sweatAlert2 
function Remind_Question(func) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Bạn chắc chắn?(你確定嗎)',
        text: "Bạn không thể hoàn nguyên việc này! (您將無法還原此內容！)",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Có (是的)',
        cancelButtonText: 'Hủy/取消',
        reverseButtons: true
    }).then(function(result) {
        if (result.isConfirmed) {
            func();
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            return false;
        }
    })
    return true;
}



//THông báo hỏi lại sweatAlert2 với tham số hàm
function Remind_Question_Option(func, option) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Bạn chắc chắn?(你確定嗎)',
        text: "Bạn không thể hoàn nguyên việc này! (您將無法還原此內容！)",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Có (是的)',
        cancelButtonText: 'Hủy/取消',
        reverseButtons: true
    }).then(function(result) {
        if (result.isConfirmed) {
            func(option);
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            return false;
        }
    })
    return true;
}



//Thông báo một tin nhắn ra màn hình
function Show_Alert_Message(message) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Thông tin lỗi!(錯誤信息！)',
        text: message,
        icon: 'warning',
        showCancelButton: false,
        confirmButtonText: ' Hủy/取消 ',
        reverseButtons: true
    })
}




//Thông báo một tin nhắn ra màn hình
function Show_Alert(title, text_btOk, message) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: title,
        text: message,
        icon: 'warning',
        showCancelButton: false,
        confirmButtonText: text_btOk,
        reverseButtons: true
    })
}