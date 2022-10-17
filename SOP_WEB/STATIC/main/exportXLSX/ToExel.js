/* <script src="{% static 'exportXLSX/xlsx.full.min.js' %}"></script> */
/* <button onclick="ExportToExcel('xlsx')">Export table to excel</button> */

function ExportToExcel(type, tableid, fn, dl) {
    var elt = document.getElementById(tableid);
    var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
    return dl ?
        XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }) :
        XLSX.writeFile(wb, fn || ('Sheet1.' + (type || 'xlsx')));
}


/* <script src="{% static 'exportXLSX/excelexportjs.js' %}"></script> */
function To_XLS(tableid) {
    $("#" + tableid).excelexportjs({
        containerid: tableid,
        datatype: 'table'
    });
}





// Lưu table to XLSX
function Save_Table_ToXLSX(tableid) {
    fnExcelReport(tableid);
}

function fnExcelReport(tableID) {
    var tab_text = "<table border='2px'><tr bgcolor='#87AFC6'>";
    var textRange;
    var j = 0;
    tab = document.getElementById(tableID); // id of table

    for (j = 0; j < tab.rows.length; j++) {
        tab_text = tab_text + tab.rows[j].innerHTML + "</tr>";
        //tab_text=tab_text+"</tr>";
    }

    tab_text = tab_text + "</table>";
    tab_text = tab_text.replace(/<A[^>]*>|<\/A>/g, ""); //remove if u want links in your table
    tab_text = tab_text.replace(/<img[^>]*>/gi, ""); // remove if u want images in your table
    tab_text = tab_text.replace(/<input[^>]*>|<\/input>/gi, ""); // reomves input params

    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) // If Internet Explorer
    {
        txtArea1.document.open("txt/html", "replace");
        txtArea1.document.write(tab_text);
        txtArea1.document.close();
        txtArea1.focus();
        sa = txtArea1.document.execCommand("SaveAs", true, "Say Thanks to Sumit.xls");
    } else //other browser not tested on IE 11
        sa = window.open('data:application/vnd.ms-excel,' + encodeURIComponent(tab_text));

    return (sa);
}