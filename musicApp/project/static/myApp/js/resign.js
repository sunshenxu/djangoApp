$(document).ready(function(){
	var $uName = $("#uName")
	var $checkName = $("#checkName")

	var $userId = $("#id")
	var $checkId = $("#checkId")
	var $checkIds = $("#checkIds")

	var $pwd = $("#pwd")
	var $checkPwd = $("#checkPwd")

	var $checkpasswd = $("#checkpasswd")
	var $checkpasswdss = $("#checkpasswdss")
	var $btn = $(".tpass-button-submit")

    var flag = false
	$uName.bind("focus",function(){
		$checkName.css("display","none")
	})
	$uName.bind("blur",function(){
		if($uName.val().length==0){
			$checkName.css("display","inline")
			// $btn.attr("disabled","disabled")
		}
		// else{
		// 	$btn.removeAttr("disabled")
		// }
	})

	$userId.bind("focus",function(){
		$checkId.css("display","none")
		$checkIds.css("display","none")
	})
	$userId.bind("blur",function(){
		if($userId.val().length<6 || $userId.val().length>12){
			$checkId.css("display","inline")
			// $btn.attr("disabled","disabled")
		}
		// else{
		// 	$btn.removeAttr("disabled")
		// }
		$.post("/checkuserid/",{"userId":$userId.val()},function(data){
			 if(data.status=='idExist'){
				$checkIds.css("display","inline")
				// $btn.attr("disabled","disabled")
                 flag = true
			}else if(data.status=='idNotExist'){
				// $btn.removeAttr("disabled")
                 flag = false
			}
		})
	})
	$pwd.bind("focus",function(){
		$checkPwd.css("display","none")
	})
	$pwd.bind("blur",function(){
		if($pwd.val().length<6 || $pwd.val().length>16){
			$checkPwd.css("display","inline")
			// $btn.attr("disabled","disabled")
		}
		// else{
		// 	$btn.removeAttr("disabled")
		// }
	})

	$checkpasswd.bind("focus",function(){
		$checkpasswdss.css("display","none")
	})
	$checkpasswd.bind("blur",function(){
		if($checkpasswd.val()!=$pwd.val()){
			$checkpasswdss.css("display","inline")
			// $btn.attr("disabled","disabled")
		}
		// else{
		// 	$btn.removeAttr("disabled")
		// }

	})
	$btn.bind("click",function(e){
		if($uName.val().length==0){
			alert("昵称不能为空！！！")
			e.preventDefault()
		}else if($userId.val().length==0){
			alert("账号不能为空！！！")
			e.preventDefault()
		}else if($pwd.val().length==0){
			alert("密码不能为空！！！")
			e.preventDefault()
		}else if($checkpasswd.val().length==0){
			alert("再次输入密码不能为空！！！")
			e.preventDefault()
		}else if($userId.val().length<6 || $userId.val().length>12){
		    alert("6-12位账号！！！")
			e.preventDefault()
        }else if($pwd.val().length<6 || $pwd.val().length>16){
		    alert("6-16位密码！！！")
			e.preventDefault()
        }else if($checkpasswd.val()!=$pwd.val()){
		    alert("两次密码不一致！！！")
			e.preventDefault()
        }else if (flag==true){
		    alert("账号已存在！！！")
			e.preventDefault()
        }

	})


})