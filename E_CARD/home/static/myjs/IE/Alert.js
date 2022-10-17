//Thông báo OK
function Alert_OK() {
    alert('Action OK');
}

//THông báo Nhập các trường dữ liệu
function Alert_Fill_data() {
    alert("Please fill all fields..");
    event.preventDefault();
}



//Thông báo NG sweatAlert2
function AlertErrorSQL(response) {
    alert("Web Server Not Excute your Action !!");
    event.defaultPrevented();
}



//THông báo OK sweatAlert2
function Alert_OK_RELOAD() {
   alert("OK");
    setTimeout(function() {
        location.reload();
    }, 1000);
}



//Thông báo một tin nhắn ra màn hình
function Show_Alert_Message(message) {
   alert(message);
   event.preventDefault();
}

function Remind_Question(func) {
  if (confirm('Are you sure you want to save this thing?')) {
    // Save it!
  func();
  } else {
    // Do nothing!
return;
  }
  
}