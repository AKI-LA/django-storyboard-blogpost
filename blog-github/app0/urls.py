from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # homepage shows list of posts
    path('post_form/', views.post_create, name='post_create'),  # page to add new post
    path('login/', views.test_login, name='login'),
]
