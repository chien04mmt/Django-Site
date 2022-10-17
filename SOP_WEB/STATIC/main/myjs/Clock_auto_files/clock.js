// Clock rotation
$(document).ready(function() {


    // var canvas = document.getElementById("canvas");
    // var ctx = canvas.getContext("2d");
    // var radius = canvas.height / 2;
    // ctx.translate(radius, radius);
    // radius = radius * 0.90
    // setInterval(drawClock, 1000);

    // function drawClock() {
    //     drawFace(ctx, radius);
    //     drawNumbers(ctx, radius);
    //     drawTime(ctx, radius);
    // }

    // function drawFace(ctx, radius) {
    //     var grad;
    //     ctx.beginPath();
    //     ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    //     ctx.fillStyle = 'white';
    //     ctx.fill();
    //     grad = ctx.createRadialGradient(0, 0, radius * 0.95, 0, 0, radius * 1.05);
    //     grad.addColorStop(0, '#333');
    //     grad.addColorStop(0.5, 'white');
    //     grad.addColorStop(1, '#333');
    //     ctx.strokeStyle = grad;
    //     ctx.lineWidth = radius * 0.1;
    //     ctx.stroke();
    //     ctx.beginPath();
    //     ctx.arc(0, 0, radius * 0.1, 0, 2 * Math.PI);
    //     ctx.fillStyle = '#333';
    //     ctx.fill();
    // }

    // function drawNumbers(ctx, radius) {
    //     var ang;
    //     var num;
    //     ctx.font = radius * 0.15 + "px arial";
    //     ctx.textBaseline = "middle";
    //     ctx.textAlign = "center";
    //     for (num = 1; num < 13; num++) {
    //         ang = num * Math.PI / 6;
    //         ctx.rotate(ang);
    //         ctx.translate(0, -radius * 0.85);
    //         ctx.rotate(-ang);
    //         ctx.fillText(num.toString(), 0, 0);
    //         ctx.rotate(ang);
    //         ctx.translate(0, radius * 0.85);
    //         ctx.rotate(-ang);
    //     }
    // }

    // function drawTime(ctx, radius) {
    //     var now = new Date();
    //     var hour = now.getHours();
    //     var minute = now.getMinutes();
    //     var second = now.getSeconds();
    //     //hour
    //     hour = hour % 12;
    //     hour = (hour * Math.PI / 6) +
    //         (minute * Math.PI / (6 * 60)) +
    //         (second * Math.PI / (360 * 60));
    //     drawHand(ctx, hour, radius * 0.5, radius * 0.07);
    //     //minute
    //     minute = (minute * Math.PI / 30) + (second * Math.PI / (30 * 60));
    //     drawHand(ctx, minute, radius * 0.8, radius * 0.07);
    //     // second
    //     second = (second * Math.PI / 30);
    //     drawHand(ctx, second, radius * 0.9, radius * 0.02);
    // }

    // function drawHand(ctx, pos, length, width) {
    //     ctx.beginPath();
    //     ctx.lineWidth = width;
    //     ctx.lineCap = "round";
    //     ctx.moveTo(0, 0);
    //     ctx.rotate(pos);
    //     ctx.lineTo(0, -length);
    //     ctx.stroke();
    //     ctx.rotate(-pos);
    // }




    // Get Date
    const date = new Date();
    let h = date.getHours() % 12;
    let m = date.getMinutes();
    let s = date.getSeconds();

    // Initialize Clock: Chia số vòng cho đồng hồ ((m * 360) / 60) / 21,
    let hA = updateClock($('.first'), Math.round((h * 360) / 12) + ((m * 360) / 60) / 10, 0);
    let mA = updateClock($('.second'), Math.round((m * 360) / 60), 0);
    let sA = updateClock($('.third'), Math.round((s * 360) / 60), 0);

    // Update Second: Cập nhật giây
    setInterval(function() {
        sA = updateClock($('.third'), sA, 0.6);
    }, 100);


    // // Update Minute
    // setInterval(function() {
    //     mA = updateClock($('.second'), mA, 1);
    // }, 10000)

    // // Update Hour
    // setInterval(function() {
    //     hA = updateClock($('.first'), hA, 1);
    // }, 50000);


    // Update Minute(Refresh After 60 second)
    setInterval(function() {
        mA = updateClock($('.second'), mA, 0.6);
    }, 6000)

    // Update Hour(Refresh After 12 minutes)
    setInterval(function() {
        hA = updateClock($('.first'), hA, 0.6);
    }, 72000);

    // Prevent overflow (Refresh After 1 hrs)
    setInterval(function() {
        window.location.reload();
    }, 1800000);

});

// Update Time
function updateClock(ref, start, add) {
    start += add;
    ref.css("transform", 'rotate(' + start + 'deg)');
    return start;
}