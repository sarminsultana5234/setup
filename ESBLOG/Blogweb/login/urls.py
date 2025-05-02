"""
URL configuration for Blogweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('landing', views.landing,name="homepage"),
# ]
   

urlpatterns = [
    path('landing', views.landing,name="myhome"),
    path('logout', views.logout_session,name="logout"),

    path('login_auth', views.login_auth,name="auth"),
    path('postuser', views.postuser,name="post_status"),

    path('deletePost', views.deletePost,name="deletePost"),
    path('myposts', views.myposts,name="myposts"),
    # path('api/test', views.api_test,name="api_test"),
    # path('api/rest', PostListApi.as_view()),

]
    

    

    
