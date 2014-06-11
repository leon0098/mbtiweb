function includeJS(src){
	document.write("<script type='text/javascript' src='/static/"+src+"'></script>");
}

function includeCSS(src){
	document.write("<link rel='stylesheet' href='/static/"+src+"'>");
}

//页面全局样式
includeCSS("css/main.css");

//全局js
includeJS("js/main.js");
