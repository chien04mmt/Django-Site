//Thông báo NG sweatAlert2
function AlertErrorSQL(response) {
    var text = response['responseJSON'];
    text = JSON.stringify(text);
    // clearInterval(yourInterval);
    Swal.fire({
        title: 'Please check Error:',
        text: text,
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Retry!'
    }).then(function(result) {

        if (result.isConfirmed) {
            if (text.includes('login')) { location.reload(); }
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


//THông báo OK sweatAlert2
function Alert_OK_RELOAD() {
    Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
    })
    setTimeout(function() {
        location.reload();
    }, 1000);
}


//THông báo Nhập các trường dữ liệu
function Alert_Fill_data() {
    Swal.fire({
        title: 'Alert!',
        text: 'Please fill all fields..',
        imageUrl: "../static/myjs/imgjs/765-400x200.jpg",
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })

}

//THông báo OK sweatAlert2
function Alert_Question() {
    var check = true;
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, Action it!',
        cancelButtonText: 'No, cancel!',
        reverseButtons: true
    }).then(function(result) {
        if (result.isConfirmed) {
            check = false;
            return check;
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            check = true
            return check;
        }
    })
    return check;
}



//THông báo hỏi lại sweatAlert2 
function Remind_Question(func) {
    Swal.fire({
        title: "您是否操作<br/>Bạn có muốn thực hiện？",
        text: "Không thể hoàn nguyên! (您將無法還原此內容！)",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#FF7043',
        confirmButtonText: "同意 / Đồng ý",
        cancelButtonText: "拒絕 / Từ chối",

    }).then((result) => {
        if (result.isConfirmed) {
            func();
        }
    })


    // const swalWithBootstrapButtons = Swal.mixin({
    //     customClass: {
    //         confirmButton: 'btn btn-success',
    //         cancelButton: 'btn btn-danger'
    //     },
    //     buttonsStyling: false
    // })

    // swalWithBootstrapButtons.fire({
    //     title: 'Bạn chắc chắn?(你確定嗎)',
    //     text: "Bạn không thể hoàn nguyên việc này! (您將無法還原此內容！)",
    //     icon: 'warning',
    //     showCancelButton: true,
    //     confirmButtonText: 'Có (是的)',
    //     cancelButtonText: 'Hủy/取消',
    //     reverseButtons: true
    // }).then(function(result) {
    //     if (result.isConfirmed) {
    //         func();
    //     } else if (
    //         /* Read more about handling dismissals below */
    //         result.dismiss === Swal.DismissReason.cancel
    //     ) {
    //         return false;
    //     }
    // })
    // return true;
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