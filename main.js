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

function Curentdate()
    { 
        var now = new Date();
        var year = now.getFullYear();       //年
        var month = now.getMonth() + 1;     //月
        var day = now.getDate();            //日       
        var date = year;
       
        if(month < 10)
            date += "0";
       
        date += month;
       
        if(day < 10)
            date += "0";
           
        date += day;
     
        return(date); 
    } 
console.log("系统时间：" + Curentdate());

var qrcode_button = document.createElement("div");
qrcode_button.innerHTML = "更改二维码";
qrcode_button.style = "position:fixed;bottom:74px;right:15px;width:102px;height:40px;background:#f92e37;color:white;text-align:center;line-height:40px;cursor:pointer;border-radius:8%;z-index:9999;";
beasetag.appendChild(qrcode_button);
qrcode_button.onclick = function change_code() {
    var image = document.getElementsByClassName("pt-17 pb-12 px-12 relative")[0].children[4];
    image.removeChild(image.children[0]);
    image.style="height:90px;width:90px;background:white;padding:5px;"
    //var url = prompt("请输入链接");
    var pdl = document.getElementsByClassName("inline-block text-14 leading-normal font-medium py-5 px-16 text-white bg-red-500 rounded-2")[0].href;
    var url = "https://store.lizhi.io/site/products/id/" + pdl.match(/[0-9]+/)[0] + "?cid=53qvofdc" + "&mtm_campaign=wechat&mtm_kwd=p" + Curentdate().toString().substr(2);
    // new QRCode(image, url);
    new QRCode(image, {
        text: url,
        width: 80,
        height: 80,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.L
    });
}

var save_button = document.createElement("div");
save_button.innerHTML = "保存为图片";
save_button.style = "position:fixed;bottom:131px;right:15px;width:102px;height:40px;background:#f92e37;color:white;text-align:center;line-height:40px;cursor:pointer;border-radius:8%;z-index:9999;";
beasetag.appendChild(save_button);
save_button.onclick = function screenshot() {
    var card = document.getElementsByClassName("bg-no-repeat bg-center bg-contain px-18 py-20 mx-auto")[0];
    var name = Curentdate().toString().substr(2) + "_" + document.getElementsByClassName("font-bold leading-none text-24")[0].innerHTML + "_qrcode";
    var icon = document.getElementsByClassName("w-105 h-105")[0];
    icon.setAttribute("crossorigin","anonymous");
    icon.src += "?";
    setTimeout(function() { 
        html2canvas(card,{
            height: 208,
            useCORS:true
           // width:1000,
           // height:416
        }).then(function(canvas) {
            //document.body.appendChild(canvas);
            canvas.toBlob(function(blob) {
                saveAs(blob, name);
             });
        });
     }, 10);
    
   
}

