# Django 编写线上教育平台

## 项目 APP 设计 
>* django app设计
   1、users   用户
   2、courses   课程
   3、organization   教育机构和教师
   4、operation  组合其他的app

### User model
>* 覆盖原有的user表
   from django.contrib.auth.models import AbstractUser
   编写自己的UserProfile继承AbstractUser
   
### 课程model
>* Course - 课程基本信息
>* Lesson - 章节信息
>* Video - 视频
>* CourseResource - 课程资源(课程源码什么的)