from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo
# Create your views here.

# def my_render(request,template_path,context_dict={}):
#     # 1、加载模板文件，模板对象
#     temp = loader.get_template(template_path)
#     # 2、定义模板上下文，给模板文件传递数据
#     context = RequestContext(request, context_dict)
#     # 3、模板渲染：产生标准的HTML内容
#     res_html = temp.render(context)
#     # 4、返回浏览器
#     return HttpResponse(res_html)

def index(request):
    return render(request,'booktest/index.html',{'content':'hello world!','list':
        list(range(0,10))})

def show_books(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',{'books':books})

def detail(request,bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()   # heroinfo_set这个方法哪里来的？？？
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})