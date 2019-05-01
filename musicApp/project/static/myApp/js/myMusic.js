$(document).ready(function () {
   $("tbody").on("mouseover",".songTime",function () {
        $(this).children(".subList").css("display",'inline-block')
    });
    $("tbody").on("mouseout",".songTime",function () {
        $(this).children(".subList").css("display",'none')
    });

    $("tbody").on("click",".subList",function () {
        var mid = $(this).attr("musicid");
        $.get("/subList/",{musicId:mid},function (data) {
            if(data.status=="notLogin"){
				window.location.assign("/login/")
			}else if(data.status=="false"){
                alert("该歌曲已不在歌单中！！！")
            }else if(data.status=="true"){
                alert("删除成功！！！");
                var id = "#"+mid;
                $(id).remove();
            }
        });
    });
});