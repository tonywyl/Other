from django.db import models

# Create your models here.


class Role(models.Model):
    name=models.CharField(max_length=48,verbose_name='名字')


class UserInfo(models.Model):
    username=models.CharField(max_length=47,verbose_name='用户名')
    email=models.EmailField(verbose_name='邮箱')
    ug=models.ForeignKey(UserGroup)
class test1(models.Model):
    title=models.CharField(max_length=74,verbose_name='标题')


class UserGroup(models.Model):
    title=models.CharField(max_length=64)




