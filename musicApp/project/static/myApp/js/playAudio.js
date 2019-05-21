$(function () {
    var mL = $("#history").attr("historyname");
    if(mL=="None"){
        var song = [
        {
            'cover': "/static/myApp/images/default.png",
            'src': 'http://music.163.com/song/media/outer/url?id=553815178.mp3',
            'title': '静悄悄'
        }
    ];
    }else {
        var song = JSON.parse(mL);    //转换为json对象
    }
    
    // var song = [
    //     {
    //         'cover': "/static/myApp/images/default.png",
    //         'src': 'http://music.163.com/song/media/outer/url?id=553815178.mp3',
    //         'title': '静悄悄'
    //     }
    // ];

    var audioFn = audioPlay({
        song: song,
        autoPlay: false  //是否立即播放第一首，autoPlay为true且song为空，会alert文本提示并退出
    });

    /* 向歌单中添加新曲目，第二个参数true为新增后立即播放该曲目，false则不播放 */
    // audioFn.newSong({
    // 	'cover' : '/static/myApp/images/default.png',
    // 	'src' : 'http://music.163.com/song/media/outer/url?id=1356499052.mp3',
    // 	'title' : '你的姑娘'
    // },false);
    /* 暂停播放 */
//	audioFn.stopAudio();

    /* 开启播放 */
//	audioFn.playAudio();

    /* 选择歌单中索引为3的曲目(索引是从0开始的)，第二个参数true立即播放该曲目，false则不播放 */
//	audioFn.selectMenu(3,true);

    /* 查看歌单中的曲目 */
    // console.log(audioFn.song);

    /* 当前播放曲目的对象 */
    // console.log(audioFn.audio);

    //实现播放功能
    $("tbody").on("click", ".play", function () {
        var title = $(this).attr("musicname");
        var id = $(this).attr("musicid");
        var src = 'http://music.163.com/song/media/outer/url?id=' + id + '.mp3';
        var img = $(this).attr("musicimg");
        var list = audioFn.song;
        for (var i = 0; i < list.length; i++) {
            if (list[i]['src'] == src) {
                list.splice(i, 1);
            }
        }

        audioFn.newSong({
            'cover': img,
            'src': src,
            'title': title
        }, true);
        var history = JSON.stringify(audioFn.song);
        $.post("/history/", {'historyList': history}, function (data) {
            if (data.status == "True") {
            }
        });
    });

    $("#player").bind("click", function () {
        var title1 = $(this).attr("musicname");
        var id1 = $(this).attr("musicid");
        var src1 = 'http://music.163.com/song/media/outer/url?id=' + id1 + '.mp3';
        var img1 = $(this).attr("musicimg");
        var list = song;
        for (var i = 0; i < list.length; i++) {
            if (list[i]['src'] == src1) {
                list.splice(i, 1);
            }
        }
        audioFn.newSong({
            'cover': img1,
            'src': src1,
            'title': title1
        }, true);
        var history = JSON.stringify(audioFn.song);
        $.post("/history/", {'historyList': history}, function (data) {
            if (data.status == "True") {
            }
        });
    });
});