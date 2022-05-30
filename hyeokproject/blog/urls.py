from django.contrib import admin
from django.urls import path
from . import views
#from hyeokproject.blog.views import delete

# 블로그가 경로로 달린 것만 남김 (팀장 느낌)
urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>', views.detail, name='detail'), # id 구분-> 패스컨버터
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('<int:blog_id>/edit', views.edit, name='edit'),
    path('<int:blog_id>/update', views.update, name='update'),
]