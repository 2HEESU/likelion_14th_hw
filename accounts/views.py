from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:postpage')
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:postpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            # 이미 있으면 메시지와 함께 가입 페이지로 다시 돌려보냄
            return render(request, 'accounts/signup.html', {'error': '이미 있는 아이디입니다!'})
        
        if request.POST['password'] == request.POST['confirm']:
            newuser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            profile = newuser.profile
            profile.nickname = request.POST['nickname']
            profile.major = request.POST['major']
            profile.profile_image = request.FILES.get('profile_image')
            profile.save()

            # nickname = request.POST['nickname']
            # major = request.POST['major']
            # age = request.POST['age']
            # profile_image = request.FILES.get('profile_image')

            # profile = Profile(
            #    user=newuser,
            #    nickname=nickname,
            #    major=major,
            #    age=age,
            #    profile_image=profile_image,
            # )
            # profile.save()
            
            auth.login(request, newuser)
            return redirect('main:postpage')
        
    return render(request, 'accounts/signup.html')