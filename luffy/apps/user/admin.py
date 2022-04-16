from django.contrib import admin

from user.models import User
from home.models import *
# Register your models here.
admin.site.site_header = "后台管理系统"
admin.site.site_title = "后台管理"
admin.site.index_title = "luffy项目"

admin.site.register(User)  # 注册user表
admin.site.register(Banner)
admin.site.register(FreeCourse)