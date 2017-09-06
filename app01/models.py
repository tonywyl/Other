from django.db import models

# Create your models here.


class UserGroup(models.Model):
    """
    用户部门表
    """
    title=models.CharField(max_length=64)
    
    def __str__(self):
        return self.title

# class Role(models.Model):
#     """
#     用户角色表
#     """
#     name=models.CharField(max_length=64)
#     def __str__(self):
#         return self.name

class UserInfo(models.Model):
    """
    用户信息表
    """
    
    user=models.CharField(max_length=64)
    email=models.EmailField()
    
    m2m=models.ForeignKey(UserGroup,null=True,blank=True)
    # u2r=models.ManyToManyField(Role)
    def __str__(self):
        return self.user
    
    
    
    




