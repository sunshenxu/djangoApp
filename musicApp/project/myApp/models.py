from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=12,unique=True)
    userName = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=20)
    userImg = models.CharField(max_length=150)
    userToken = models.CharField(max_length=50)
    userRank = models.IntegerField()
    # isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'user'
    @classmethod
    def createUser(cls,userId,userName,userPwd,userImg,userToken,userRank):
        user = cls(userId,userName,userPwd,userImg,userToken,userRank)
        return user