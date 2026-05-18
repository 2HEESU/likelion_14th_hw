from django.urls import path

from . import views
from .views import *

app_name = 'main'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('new_post/', new_post, name='new_post'),
    path('create/', create, name='create'),
    path('post/', postpage, name='postpage'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('edit/<int:post_id>', edit, name='edit'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),
    path('comment_delete/<int:comment_id>', comment_delete, name='comment_delete'),
    path('comment_edit/<int:comment_id>', comment_edit, name='comment_edit'),
    path('comment_update/<int:comment_id>', comment_update, name='comment_update'),
    path('tags', tag_list, name='tag_list'),
    path('tags/<int:tag_id>', tag_post_list, name='tag_post_list'),
    path('likes/<int:post_id>', likes, name='likes'),
    path('comment_likes/<int:comment_id>', comment_likes, name='comment_likes'),
]