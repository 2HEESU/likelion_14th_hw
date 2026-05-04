from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')

def mainpage(request):
    context = {
        'generation': 14, 
        'topic1': {
            'title': '1. Django의 기본 구조: Project와 App',
            'content': [
                'Project는 하나의 웹 서비스 전체를 의미하는 큰 단위 (인스타그램)',
                'App은 프로젝트를 구성하는 기능별 집합 단위 (회원정보 관리 기능, 게시글 기능 등)'
            ]
        },

        'topic2': {
            'title': '2. HTML / VIEW / URL 파트 정리',
            'content': [
                'templates/앱이름/ 폴더 구조를 통해 템플릿 파일명이 겹치는 것을 방지★',
                'View는 render 함수를 통해 HTML을 렌더링하여 사용자에게 응답',
                "urls.py의 빈 경로('')는 웹사이트의 첫 페이지(루트 URL)를 의미"
            ]
        },

        'topic3': {
            'title': '3. Django Template 언어 정리',
            'content': [
                "{% url 'name' %}으로 페이지 간 이동 링크를 쉽게 연결",
                "{{ variable }} 형태로 데이터를 출력하며 점(.)으로 속성에 접근★",
                "{% for %}와 {% if %}로 반복문과 조건문 로직을 구현"
            ]
        },

        'topic4': {
            'title': '4. 중복되는 HTML 파일 정리',
            'content': [
                'base.html을 통해 공통 레이아웃을 작성하고 상속 구조 생성',
                '{% block content %} 내부에 각 페이지의 개별 내용을 채우기★',
                '{% extends %} 태그는 반드시 HTML 최상단에 선언★',
                '{% include %}를 활용해 내비게이션 바 등 컴포넌트를 분리 관리'
            ]
        },
        
        'topic5': {
            'title': '5. 정적 파일 분리 정리',
            'content': [
                'static 폴더 내부에 css, images 폴더를 만들어 체계적으로 관리',
                'HTML 상단에 {% load static %}을 선언하여 정적 파일을 불러옴',
                'settings.py에서 STATICFILES_DIRS 경로를 설정해야 장고가 파일을 찾을 수 있음★'
            ]
        }
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {
        'name': '이희수',
        'age': '22살',
        'major': '정보통신공학과',
        'lookalike': '검정고양이🐈‍⬛',
        'mbti': 'ISTP',
        'hobbies': ['옷 아이쇼핑', '공포 추리 소설 읽기', '느좋 공간 찾기'],
        'aspiration': '1년동안 열심히 배우겠습니다!'
    }
    return render(request, 'main/secondpage.html', context)

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    return render(request, 'main/new_post.html')

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    new_post = Post()

    new_post.title = request.POST['title']
    new_post.writer = request.user.username
    new_post.pub_date = request.POST['pub_date']
    new_post.content = request.POST['content']
    new_post.hits = request.POST['hits']

    new_post.save()

    return redirect('main:detail', new_post.id)

def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.hits += 1
    post.save()
    return render(request, 'main/detail.html', {'post':post})

def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id)

    if edit_post.writer != request.user.username:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {"post":edit_post})

def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    update_post = get_object_or_404(Post, pk=post_id)

    if update_post.writer != request.user.username:
        return redirect('main:detail', update_post.id)
    
    update_post.title = request.POST['title']
    update_post.writer = request.user.username
    update_post.pub_date = request.POST['pub_date']
    update_post.content = request.POST['content']
    update_post.save()

    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_post = get_object_or_404(Post, pk=post_id)

    if delete_post.writer != request.user.username:
        return redirect('main:detail', delete_post.id)
    
    delete_post.delete()

    return redirect('main:postpage')