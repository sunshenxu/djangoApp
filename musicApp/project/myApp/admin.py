from django.contrib import admin

# Register your models here.
from myApp.models import User, Musci


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def userName(self):
        return self.userName
    userName.short_description = "姓名"

    def userPwd(self):
        return self.userPwd
    userPwd.short_description = "密码"

    def userImg(self):
        return self.userImg
    userImg.short_description = "头像"

    def userRank(self):
        return self.userRank
    userRank.short_description = "等级"

    list_display = ['id', userName, userPwd, userImg, 'userToken', userRank]
    list_per_page = 10
    search_fields = ['userName']

@admin.register(Musci)
class MusciAdmin(admin.ModelAdmin):
    def musicName(self):
        return self.musicName
    musicName.short_description = "歌曲名"

    def musicTime(self):
        return self.musicTime
    musicTime.short_description = "时长"

    def musicOuther(self):
        return self.musicOuther
    musicOuther.short_description = "作者"

    def lyricContent(self):
        return self.lyricContent
    lyricContent.short_description = "歌词"

    def musicImg(self):
        return self.musicImg
    musicImg.short_description = "头像"

    list_display = ['id', musicName, musicTime, musicOuther, lyricContent, musicImg]
    list_per_page = 10
    search_fields = ['musicName']