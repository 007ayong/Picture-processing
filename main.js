var mybutton,beasetag;
mybutton = document.createElement("div");
beasetag = document.querySelector("body");
beasetag.appendChild(mybutton);
mybutton.innerHTML = "更改价格";
mybutton.style = "position:fixed;bottom:17px;right:15px;width:102px;height:50px;background:#f92e37;color:white;text-align:center;line-height:50px;cursor:pointer;border-radius:8%;z-index:9999;";
mybutton.onclick = function change_price(){
    var new_price = prompt("请输入价格，如：6.18 起");
    var price = document.getElementsByClassName("text-blue-600 text-22 font-semibold");
    price[0].innerHTML='<span class="text-14 font-normal">￥</span>'+new_price;
}

