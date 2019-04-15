from django.shortcuts import render,redirect
import os
from django.conf import settings
import time,random
from .models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    name = request.session.get('username','未登录')
    return render(request,'myApp/index.html',{'title':name})

def login(request):
    if request.method == 'POST':
        try:
            userId = request.POST.get('userId')
            if request.POST.get('passwd') == User.userobj.get(userId=userId).userPwd:
                request.session['username'] = User.userobj.get(userId=userId).userName
                request.session['token'] = str(time.time() + random.randrange(0,100000))
                return redirect('/index/')
            else:
                return HttpResponse("密码错误")
        except User.DoesNotExist as e:
            return HttpResponse("账号不存在")
    else:
        return render(request,'myApp/login.html')

def resign(request):
    if request.method == 'POST':
        userId = request.POST.get('userId')
        userPwd = request.POST.get('userPwd')
        userName = request.POST.get('userName')
        userRank = 0
        f = request.FILES.get('userImg')
        filePath = os.path.join(settings.MDEIA_ROOT,userId+'.jpg')
        userImg = filePath
        with open(filePath,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
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