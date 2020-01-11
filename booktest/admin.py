from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# Register your models here.

# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','b_pubdate']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcomment','hgender','hbook']

# 注册模型
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)