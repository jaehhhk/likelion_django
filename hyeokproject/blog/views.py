#from urllib import request
from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def new(request):
    return render(request, 'new.html') # new.html 띄워줌

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #현재시간 가져옴 임포트 해줘야 위에
    blog.save()
    return redirect('/blog/' + str(blog.id))    #render은 html 파일을 던저주지만, render은 url 던저줌 -> 빈 url인 '/'이면 메인 페이지에 던저줌
                                                #'/blog/' + str(blog.id) -> 메인페이지+브롤그 아이디 -> 해당 글로 바로
def detail(request, blog_id):
    blog_detail = Blog.objects.get(id = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def delete(request, blog_id):
    Blog.objects.get(id = blog_id).delete()
    return redirect('/')

def edit(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.title = request.POST.get('title')  #post 방식
    blog.body = request.POST.get('body')
    blog.pub_date = timezone.datetime.now() #현재시간 가져옴 임포트 해줘야 위에
    blog.save()
    return redirect('/blog/' + str(blog.id))