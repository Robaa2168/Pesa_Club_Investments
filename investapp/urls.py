
  #  path('users/', views.manage_student, name="users.html"),
from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from investapp import views as user_views


urlpatterns=[
    path('index',views.index,name = 'index'),
    # path('register/', views.registerPage, name="register"),
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
]