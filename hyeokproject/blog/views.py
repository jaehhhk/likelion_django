#from urllib import request
from django.shortcuts import redirect, render
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects

    blog_list = Blog.objects.all()  # 모든 객체 담아라
    paginator = Paginator(blog_list, 2) # 장고에서 기본 제공 함수, 2개씩 담아 나눠라
    page = request.GET.get('page')  # 현재 페이지 값
    posts = paginator.get_page(page)    # 페이지값을 html에 넘겨준다

    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

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