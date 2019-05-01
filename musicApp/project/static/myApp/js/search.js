$(document).ready(function () {
   $("tbody").on("mouseover",".songTime",function () {
        $(this).children(".addList").css("display",'inline-block')
    });
    $("tbody").on("mouseout",".songTime",function () {
        $(this).children(".addList").css("display",'none')
    });

    $("tbody").on("click",".addList",function () {
        var mid = $(this).attr("musicid");
        $.get("/addList/",{musicId:mid},function (data) {
            if(data.status=="notLogin"){
				window.location.assign("/login/")
			}else if(data.status=="false"){
                alert("该歌曲已在歌单中！！！")
            }else if(data.status=="true"){
                alert("添加成功！！！")
            }
        });
    });
});