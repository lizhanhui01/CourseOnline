# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#定义model - Django已经为我们默认定义了一个user表


class UserProfile(AbstractUser):

    # 继承原有的user属性之后  在下面加入我们自己特有的属性
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday=models.DateField(validators=u"生日",null=True,blank=True)
    gender=models.CharField(choices=(("male",u"男"),("famale","女")),default="female",max_length=5)
    address=models.CharField(max_length=100,default="")
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username

    pass



