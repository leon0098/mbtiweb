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

//jquery
includeJS("plugin/jquery-ui-1.10.4/js/jquery-1.10.2.js");

//jquery ui
includeCSS("plugin/jquery-ui-1.10.4/css/redmond/jquery-ui-1.10.4.custom.css");
includeJS("plugin/jquery-ui-1.10.4/js/jquery-ui-1.10.4.custom.js");