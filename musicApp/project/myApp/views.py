from django.shortcuts import render,redirect
import os
from django.conf import settings
import time,random
import json

from django.views.decorators.csrf import csrf_exempt

from .models import User,Musci
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    name = request.session.get('username','未登录')
    start = 0
    limit = 50
    if request.is_ajax():
        start = int(request.GET.get("start"))
        limit = int(request.GET.get("limit"))
        musicList = Musci.objects.all()[start:start + limit]
        mL = []
        for item in musicList:
            m = {
                'name':item.musicName,
                'time':item.musicTime,
                'outher':item.musicOuther,
                'id':item.musicId,
            }
            mL.append(m)
        # musicLJ = {
        #     'music':mL
        # }
        # musicJson = json.dumps(musicLJ)
        return JsonResponse({"music":mL})
    music = Musci.objects.all()[start:start+limit]
    if name == "未登录":
        return render(request, 'myApp/index.html', {'title': "主页", 'userName': name, "music": music,"src":"default.png"})
    userId = request.session.get('userId')
    user = User.userobj.get(userId=userId)
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/index.html',{'title':"主页",'userName':name,"music":music,"src":src})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            userId = request.POST.get('userId')
            if request.POST.get('passwd') == User.userobj.get(userId=userId).userPwd:
                request.session['username'] = User.userobj.get(userId=userId).userName
                request.session['token'] = str(time.time() + random.randrange(0,100000))
                request.session['userId'] = userId
                return JsonResponse({"status":"true"})
            else:
                return JsonResponse({"status":"pwdError"})
        except User.DoesNotExist as e:
            return JsonResponse({"status":"idNot"})
    else:
        return render(request,'myApp/login.html')

def resign(request):
    if request.method == 'POST':
        userId = request.POST.get('userId')
        userPwd = request.POST.get('userPwd')
        userName = request.POST.get('userName')
        userRank = 0

        userImg = os.path.join(settings.MDEIA_ROOT,'default.png')
        userToken = str(time.time() + random.randrange(0,100000))
        user = User.userobj.createUser(userId,userName,userPwd,userImg,userToken,userRank)
        user.save()
        request.session['username'] = userName
        request.session['token'] = userToken
        request.session['userId'] = userId
        return redirect('/index/')
    else:
        return render(request,'myApp/resign.html')

def out(request):
    logout(request)
    return redirect('/index/')


@csrf_exempt
def checkuserid(request):
    userId = request.POST.get("userId")
    try:
        user = User.userobj.get(userId=userId)
        return JsonResponse({"status":"idExist"})
    except User.DoesNotExist:
        return JsonResponse({"status": "idNotExist"})

def search(request):
    name = request.session.get('username', '未登录')
    if name == "未登录":
        return redirect('/login/')
    musicname = request.POST.get("search")
    searchList = Musci.objects.filter(musicName__contains=musicname)
    userId = request.session.get('userId')
    user = User.userobj.get(userId=userId)
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/search.html',{'searchList':searchList,'title':"搜索结果",'userName':name,'src':src})

#歌词页面
def info(request,id):
    try:
        name = request.session.get('username', '未登录')
        if name == "未登录":
            return redirect('/login/')
        music = Musci.objects.get(musicId=id)
        userId = request.session.get('userId')
        user = User.userobj.get(userId=userId)
        src = user.userImg.split("\\")[-1]
        return render(request,'myApp/info.html',{'title':"歌词",'userName':name,'music':music,'src':src})
    except Musci.DoesNotExist as e:
        return HttpResponse("歌曲不存在")

def userInfo(request):
    name = request.session.get('username', '未登录')
    if name == "未登录":
        return redirect('/login/')
    userId = request.session.get('userId')
    user = User.userobj.get(userId = userId)
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/userInfo.html',{"user":user,'userName':name,'title':"个人信息","src":src})


def upImage(request):
    name = request.session.get('username', '未登录')
    if name == "未登录":
        return redirect('/login/')
    return render(request,"myApp/upImage.html")


def changeImage(request):
    f = request.FILES.get('userImg')
    userId = request.session.get('userId')
    filePath = os.path.join(settings.MDEIA_ROOT,userId+'.jpg')
    userImg = filePath
    user = User.userobj.get(userId=userId)
    user.userImg = userImg
    user.save()
    with open(filePath,'wb') as fp:
        for data in f.chunks():
            fp.write(data)
    return redirect("/index/")