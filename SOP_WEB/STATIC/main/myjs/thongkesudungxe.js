//Lấy dữ liệu tìm kiếm gửi qua server
function Get_search_data() {
    return {
        CAR_NUMCARD: $("#CARNO").val(),
        LEAVE_TIME: $("#LEAVE_TIME").val(),
        ARRIVE_TIME: $("#ARRIVE_TIME").val()
    }
}

//Tìm kiếm thống kê
function TIMKIEM_THONGKE() {
    var data = Get_search_data();
    // if (CHECK_ARR_NOT_NULL(data) == false) { return false; }

    $.ajax({
        type: 'GET',
        url: '/timkiem_thongkesd/',
        data: data,
        success: function(response) {
            $("#table_thongkesd").DataTable().destroy();
            $("#tbody_thongkesd").empty();
            try {
                response['returndata'].forEach(function FILL_DATA(item, index) {
                    $("#tbody_thongkesd").append(
                        `<tr>
                            <td><i class="fa fa-envelope f-16 text-c-green" aria-hidden="true"></i></td>
                            <td id="DOC_NO_` + item['DOC_NO'] + `">` + item['DOC_NO'] + `</td>
                            <td>` + item['Dept'] + `</td>
                            <td>` + item['CODE_NO'] + `</td>
                            <td>` + item['CARNUM'] + `</td>
                            <td>` + item['LEAVE_TIME'] + `</td>
                            <td>` + item['ROUTE'] + `</td>
                            <td>` + item['LEAVE_TIME'] + `</td>
                            <td>` + item['ARRIVE_TIME'] + `</td>
                            <td>` + item['OVERTIME'] + `</td>
                            <td>` + item['KILOMET'] + `</td>
                        </tr>`
                    );
                });
                $("#table_thongkesd").DataTable();
            } catch (err) {
                location.reload();
            }

        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}


//# xuất thông tin thống kê đồng hồ đo
function PRINT_THONGKE_DONGHODO() {
    var td = document.querySelectorAll("#tbody_thongkesd > tr > td");
    var chuoi = '';
    $(td).each(function SEARCH(index, value) {
        if ((this.id).includes('DOC_NO_') == true) {
            chuoi += $(this).text() + ",";
        }
    });
    // console.log(chuoi);
    var data = {
        DOC_NO: chuoi
    }

    $.ajax({
        type: 'GET',
        url: "/thongke_donghodo/",
        data: data,
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {
            Alert_OK();
            // try {
            //     var link = document.createElement('a'),
            //         filename = fname;
            //     link.href = URL.createObjectURL(data);
            //     link.download = filename;
            //     link.click();
            // } catch (err) {
            //     location.reload();
            // }
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}


//Xuất thông tin thống kê mức sử dụng theo biển số
function PRINT_THONGKE_THEOBIENSO() {
    var data = Get_search_data();

    $.ajax({
        type: 'GET',
        url: "/thongke_bienso/",
        data: data,
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {

            try {
                var link = document.createElement('a'),
                    filename = 'Thongkebienso.xlsx';
                link.href = URL.createObjectURL(data);
                link.download = filename;
                link.click();
            } catch (err) {
               alert(err);
            }
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}


//Xuất thông tin thống kê tổng xe sử dụng theo năm
function PRINT_THONGKE_THEONAM() {
    var data = {
        year: $("#year").val(),
    }
    if (CHECK_ARR_NOT_NULL(data) == false) { return false; }
    $.ajax({
        type: 'GET',
        url: "/thongke_theonam/",
        data: data,
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {
            try {
                var link = document.createElement('a'),
                    filename = 'Thongketheonam.xlsx';
                link.href = URL.createObjectURL(data);
                link.download = filename;
                link.click();
            } catch (err) {
                location.reload();
            }
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}


//Thống kê đi chung
function PRINT_THONGKE_DICHUNG() {
    var data = Get_search_data();
    // if (CHECK_ARR_NOT_NULL(data) == false) { return false; }
    $.ajax({
        type: 'GET',
        url: "/thongke_dichungxe/",
        data: data,
        dataType: 'binary',
        xhrFields: {
            'responseType': 'blob'
        },
        success: function(data, status, xhr) {
            try {
                var link = document.createElement('a'),
                    filename = 'Thongkedichung.xlsx';
                link.href = URL.createObjectURL(data);
                link.download = filename;
                link.click();
            } catch (err) {
                alert(err);
                location.reload();
            }
        },
        error: function(response) {
            AlertErrorSQL(response);
        }
    });
}