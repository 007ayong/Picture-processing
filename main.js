var mybutton,beasetag;
mybutton = document.createElement("div");
beasetag = document.querySelector("body");
beasetag.appendChild(mybutton);
mybutton.innerHTML = "更改价格";
mybutton.style = "position:fixed;bottom:17px;right:15px;width:102px;height:40px;background:#f92e37;color:white;text-align:center;line-height:40px;cursor:pointer;border-radius:8%;z-index:9999;";
mybutton.onclick = function change_price(){
    var new_price = prompt("请输入价格，如：6.18 起");
    var price = document.getElementsByClassName("text-blue-600 text-22 font-semibold");
    price[0].innerHTML='<span class="text-14 font-normal">￥</span>'+new_price;
}

var qrcode_button = document.createElement("div");
qrcode_button.innerHTML = "更改二维码";
qrcode_button.style = "position:fixed;bottom:70px;right:15px;width:102px;height:40px;background:#f92e37;color:white;text-align:center;line-height:40px;cursor:pointer;border-radius:8%;z-index:9999;";
beasetag.appendChild(qrcode_button);
qrcode_button.onclick = function change_code() {
    var image = document.getElementsByClassName("pt-17 pb-12 px-12 relative")[0].children[4];
    image.removeChild(image.children[0]);
    image.style="height:90px;width:90px;background:white;padding:5px;"
    var url = prompt("请输入链接");
    // new QRCode(image, url);
    new QRCode(image, {
        text: url,
        width: 80,
        height: 80,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
}

