$(document).ready(function(){
	var $userId = $("#id")
	var $checkId = $("#checkId")
	var $pwd = $("#pwd")
	var $checkPwd = $("#checkPwd")
	var $btn = $(".tpass-button-submit")
	$userId.bind("focus",function(){
		$checkId.css("display","none")
	})
	$userId.bind("blur",function(){
		if($userId.val().length<6 || $userId.val().length>12){
			$checkId.css("display","inline")
			$btn.attr("disabled","disabled")
		}else{
			$btn.removeAttr("disabled")
		}
	})
	$pwd.bind("focus",function(){
		$checkPwd.css("display","none")
	})
	$pwd.bind("blur",function(){
		if($pwd.val().length<6 || $pwd.val().length>16){
			$checkPwd.css("display","inline")
			$btn.attr("disabled","disabled")
		}else{
			$btn.removeAttr("disabled")
		}
	})
})