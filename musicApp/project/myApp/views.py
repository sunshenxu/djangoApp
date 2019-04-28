from django.shortcuts import render,redirect
import os
from django.conf import settings
import time,random
import json

from django.views.decorators.csrf import csrf_exempt

from .models import User,Musci,myMusicList
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
                'img':item.musicImg
            }
            mL.append(m)
        # musicLJ = {
        #     'music':mL
        # }
        # musicJson = json.dumps(musicLJ)
        return JsonResponse({"music":mL})
    music = Musci.objects.all()[start:start+limit]
    token = request.session.get('token')
    if token==None:     #这里应该用token值验证登录
        return render(request, 'myApp/index.html', {'title': "主页", 'userName': name, "music": music,"src":"default.png"})
    user = User.userobj.get(userToken=token)
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/index.html',{'title':"主页",'userName':name,"music":music,"src":src})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            userId = request.POST.get('userId')
            user = User.userobj.get(userId=userId)
            if request.POST.get('passwd') == user.userPwd:
                request.session['username'] = user.userName
                token = str(time.time() + random.randrange(0,100000))
                request.session['token'] =  token   #这里应要把token值存入数据库中
                user.userToken = token
                user.save()
                return JsonResponse({"status":"true"})      #使用ajax，不能在这里使用重定向
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
    token = request.session.get('token')
    if token == None:
        return redirect('/login/')
    musicname = request.GET.get("search")
    searchList = Musci.objects.filter(musicName__contains=musicname)[0:20]
    user = User.userobj.get(userToken=token)
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/search.html',{'searchList':searchList,'title':"搜索结果",'userName':name,'src':src})

#歌词页面
def info(request,id):
    try:
        name = request.session.get('username', '未登录')
        token = request.session.get('token')
        if token == None:
            return redirect('/login/')
        music = Musci.objects.get(musicId=id)
        user = User.userobj.get(userToken=token)    #可以使用token值获取该用户
        src = user.userImg.split("\\")[-1]
        return render(request,'myApp/info.html',{'title':"歌词",'userName':name,'music':music,'src':src})
    except Musci.DoesNotExist as e:
        return HttpResponse("歌曲不存在")

def userInfo(request):
    name = request.session.get('username', '未登录')
    token = request.session.get('token')
    if token == None:
        return redirect('/login/')
    try:
        user = User.userobj.get(userToken=token)
    except User.DoesNotExist as e:
        return HttpResponse("用户不存在")
    src = user.userImg.split("\\")[-1]
    return render(request,'myApp/userInfo.html',{"user":user,'userName':name,'title':"个人信息","src":src})


def upImage(request):
    token = request.session.get('token')
    if token == None:
        return redirect('/login/')
    return render(request,"myApp/upImage.html")


def changeImage(request):
    f = request.FILES.get('userImg')
    token = request.session.get('token')
    user = User.userobj.get(userToken=token)
    userId = user.userId
    filePath = os.path.join(settings.MDEIA_ROOT,userId+'.jpg')
    userImg = filePath
    user.userImg = userImg
    user.save()
    with open(filePath,'wb') as fp:
        for data in f.chunks():
            fp.write(data)
    return redirect("/index/")

def myList(request):
    userId = '111111'
    musicId = "1111"
    musicName = "111111"
    musicTime = "124"
    musicOuther = "222"
    musicImg = "535"
    list = myMusicList.createList(userId,musicId,musicName,musicTime,musicOuther,musicImg)
    list.save()
    return HttpResponse("sss")