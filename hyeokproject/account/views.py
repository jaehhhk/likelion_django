from django.shortcuts import render, redirect
from django.contrib.auth.models import User # User: 장고에서 기본 제공 모델
from django.contrib import auth
#get은 만족하는 맨 첫번째 값, filter은 만족하는 모든 값 반환
# Create your views here.
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error': '이미 있는 사용자입니다.'})
    
        if password == request.POST['passwordCheck']:
            user = User.objects.create_user(
                username, password = password
            )
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error': "비밀번호 일치안함"})

    else:
        return render(request, 'signup.html')