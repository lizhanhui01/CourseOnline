# Django 编写线上教育平台

>* django app设计
   1、users   用户
   2、courses   课程
   3、organization   教育机构和教师
   4、operation  组合其他的app


>* 覆盖原有的user表
   from django.contrib.auth.models import AbstractUser
   编写自己的UserProfile继承AbstractUser