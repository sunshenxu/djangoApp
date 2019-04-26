$(function(){
	var song = [
		{
			'cover' : "/static/myApp/images/default.png",
			'src' : 'http://music.163.com/song/media/outer/url?id=38576323.mp3',
			'title' : '春风十里'
		},
		{
			'cover' : '/static/myApp/images/default.png',
			'src' : 'http://music.163.com/song/media/outer/url?id=531295576.mp3',
			'title' : '最美的期待'
		},
		{
			'cover' : '/static/myApp/images/default.png',
			'src' : 'http://music.163.com/song/media/outer/url?id=368794.mp3',
			'title' : '牡丹江'
		},
		{
			'cover' : '/static/myApp/images/default.png',
			'src' : 'http://music.163.com/song/media/outer/url?id=26217171.mp3',
			'title' : '有可能的夜晚'
		},
		{
			'cover' : '/static/myApp/images/default.png',
			'src' : 'http://music.163.com/song/media/outer/url?id=526646591.mp3',
			'title' : '（笑）'
		}
	];

	var audioFn = audioPlay({
		song : song,
		autoPlay : false  //是否立即播放第一首，autoPlay为true且song为空，会alert文本提示并退出
	});

	/* 向歌单中添加新曲目，第二个参数true为新增后立即播放该曲目，false则不播放 */
	audioFn.newSong({
		'cover' : '/static/myApp/images/default.png',
		'src' : 'http://music.163.com/song/media/outer/url?id=1356499052.mp3',
		'title' : '你的姑娘'
	},false);
	/* 暂停播放 */
//	audioFn.stopAudio();

	/* 开启播放 */
//	audioFn.playAudio();

	/* 选择歌单中索引为3的曲目(索引是从0开始的)，第二个参数true立即播放该曲目，false则不播放 */
//	audioFn.selectMenu(3,true);

	/* 查看歌单中的曲目 */
	// console.log(audioFn.song);

	/* 当前播放曲目的对象 */
//	console.log(audioFn.audio);

	//实现播放功能
    $(".play").bind("click",function () {
		var title = $(this).attr("musicname");
		var id = $(this).attr("musicid");
		var src = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3';
        audioFn.newSong({
		'cover' : '/static/myApp/images/default.png',
		'src' : src,
		'title' : title
	},true);
    });

    $("#player").bind("click",function () {
		var title1 = $(this).attr("musicname");
		var id1 = $(this).attr("musicid");
		var src1 = 'http://music.163.com/song/media/outer/url?id='+id1+'.mp3';
        audioFn.newSong({
		'cover' : '/static/myApp/images/default.png',
		'src' : src1,
		'title' : title1
	},true);
    });
});