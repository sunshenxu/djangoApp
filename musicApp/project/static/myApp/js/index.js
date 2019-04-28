$(document).ready(function () {
    function getDocumentTop() {
    var scrollTop = 0, bodyScrollTop = 0, documentScrollTop = 0;
    if (document.body) {
        bodyScrollTop = document.body.scrollTop;
    }
    if (document.documentElement) {
        documentScrollTop = document.documentElement.scrollTop;
    }
    scrollTop = (bodyScrollTop - documentScrollTop > 0) ? bodyScrollTop : documentScrollTop;
    return scrollTop;
}

//可视窗口高度
function getWindowHeight() {
    var windowHeight = 0;
    if (document.compatMode == "CSS1Compat") {
        windowHeight = document.documentElement.clientHeight;
    } else {
        windowHeight = document.body.clientHeight;
    }
    return windowHeight;
}

//滚动条滚动高度
function getScrollHeight() {
    var scrollHeight = 0, bodyScrollHeight = 0, documentScrollHeight = 0;
    if (document.body) {
        bodyScrollHeight = document.body.scrollHeight;
    }

    if (document.documentElement) {
        documentScrollHeight = document.documentElement.scrollHeight;
    }
    scrollHeight = (bodyScrollHeight - documentScrollHeight > 0) ? bodyScrollHeight : documentScrollHeight;
    return scrollHeight;
}


/*
当滚动条滑动，触发事件，判断是否到达最底部
然后调用ajax处理函数异步加载数据
*/
var lim = 50;
var st = 0;
window.onscroll = function () {
    //监听事件内容
    if (getScrollHeight() == getWindowHeight() + getDocumentTop()) {
        //当滚动条到底时,这里是触发内容
        //异步请求数据,局部刷新dom
        st += lim;
        ajax_function();
    }
}
function ajax_function() {
    $.get('/index/',{start:st,limit:lim},function (data) {
        // console.log(data.music);
        var j = st+1;
        for(var i=0;i<data.music.length;i++){
            var $tr = $('<tr class="ls"><td class="order"><div class="par"><span class="num">'+j+'</span><span class="play" musicname="'+data.music[i].name+'" musicid="'+data.music[i].id+'" musicimg="'+data.music[i].img+'"><img src="/static/myApp/images/pl.jpg" title="播放"/></span></div></td><td class="songName"><a href="/index/'+data.music[i].id+'/" title="'+data.music[i].name+'"><div>'+data.music[i].name+'</div></a></td><td class="songTime"><span>'+data.music[i].time+'</span></td><td class="songer"><a href="" title="'+data.music[i].outher+'"><div>'+data.music[i].outher+'</div></a></td></tr>');
            $("tbody").append($tr);
            j++;
        }
    })
}


});