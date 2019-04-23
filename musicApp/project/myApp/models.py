from django.db import models

# Create your models here.
class userManager(models.Manager):
    def createUser(self,userId,userName,userPwd,userImg,userToken,userRank):
        user = self.model()
        user.userId = userId
        user.userName = userName
        user.userPwd = userPwd
        user.userImg = userImg
        user.userToken = userToken
        user.userRank = userRank
        return user

class User(models.Model):
    userobj = userManager()
    userId = models.CharField(max_length=12,unique=True)
    userName = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=20)
    userImg = models.CharField(max_length=150)
    userToken = models.CharField(max_length=50)
    userRank = models.IntegerField()
    # isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'user'
    # @classmethod
    # def createUser(cls,userId,userName,userPwd,userImg,userToken,userRank):
    #     user = cls(userId,userName,userPwd,userImg,userToken,userRank)
    #     return user


class Musci(models.Model):
    musicId = models.CharField(max_length=30,unique=True)
    musicName = models.CharField(max_length=30)
    musicTime = models.CharField(max_length=20)
    musicOuther = models.CharField(max_length=30)
    # lyricContent = models.CharField(max_length=400)
    lyricContent = models.TextField()
    musicImg = models.CharField(max_length=100)


    class Meta:
        db_table = 'music'