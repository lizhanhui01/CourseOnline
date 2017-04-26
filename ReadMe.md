# Django 编写线上教育平台

## 项目 APP 设计 
>* django app设计   
   1、users   用户   
   2、courses   课程   
   3、organization   教育机构和教师   
   4、operation  组合其他的app   
   
##新建APP
>* 1、Pycharm 中：Tools -> Rum manage.py Task -> startapp app_name   
>* 2、terminal中：cd 到项目的根目录 -> startapp app_name

## User app
###user表的编写（要覆盖原有的user表）
>* 覆盖原有的user表
   from django.contrib.auth.models import AbstractUser    
   编写自己的UserProfile继承AbstractUser
   
## 课程 app
###表的编写
>* Course - 课程基本信息   
>* Lesson - 章节信息    
>* Video - 视频     
>* CourseResource - 课程资源(课程源码什么的)      

###Django中外键的使用
>* Class Course(models.Model):     
       //TODO      
   Class CourseResource(models.Model):      
       course = models.ForeignKey(Course,verbose_name=u"课程")
       
       
## 后台管理系统
### 特点：
>* 权限管理
>* 少前端样式
>* 快速开发


##出现的问题
### 1、把apps文件夹Mark为Sources Root，在项目的导入中没有问题，但是在用本地的Python运行时却会报错
>* 因为本地Python是不知道我们把apps这个文件夹作为了资源的根目录的，所以Python在读取module时找不到我们自己定义的APP
>* 我们应该告诉Python我们把那些文件夹作为了SourcesRoot，那么怎么告诉呢，在setting中定义(18-19)行，这里我就不写了
       

##使用xadmin
>* 1、安裝后xadmin后，再setting的APP中导入xadmin以及crispy_forms
>* 2、把urls.py中的启动项目的指向admin的URL该为指向xadmin
>* 3、导入xadmin的数据库表 Tools->run manage.py task->makemigrations->migrate
>* 4、启动时访问http://127.0.0.1:8000/是会报错的 - 这正常，访问http://127.0.0.1:8000/xadmin/就行

