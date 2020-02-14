from django.urls import path, Resolver404
from django.conf.urls import handler404
# from django.core.management.base import SystemCheckError
from .views import *
# from .views import Error_404

handler404 = 'blog.views.Error_404'

urlpatterns = [
    path('', Index.as_view(), name='index'), #Index page
    path('post/new/', post_new.as_view(), name='post_new'), #Create  pageform
    path('post/<str:slug>', PostDatail.as_view(), name='post_det'), # Page for post
    path('post/<str:slug>/edit', post_edit.as_view(), name='post_edit'), # Page for post
    path('post/<str:slug>/del', post_edit.as_view(), name='post_del'), # Page for post
    path('tags/', tag_list.as_view(), name='tag_list'), # Tag list page
    path('tag/new/', tag_new.as_view(), name='tag_new'), #Create Tag pageform
    path('tag/<str:slug>', tag_detail.as_view(), name='tag_det'), #Posts from selected tag
    path('tag/<str:slug>/del', tag_delete.as_view(), name='tag_del'),  # Posts from selected tag
    path('tag/<str:slug>/edit', tag_edit.as_view(), name='tag_edit') #Posts from selected tag
]
