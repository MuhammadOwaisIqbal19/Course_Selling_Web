"""
URL configuration for courseselling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .views import create_course,add_update_content,CustomLoginView,mark_video_watched


urlpatterns = [
    path("create_course",create_course,name='create_course'),
    path("add_update_content/<int:course_id>/",add_update_content,name='add_update_content'),
    path('registration/login/', CustomLoginView.as_view(), name='login'),
    path('mark-video-watched/', mark_video_watched, name='mark_video_watched'),
    
    # path('', include('django.contrib.auth.urls')),  # Includes login, logout, password management URLs
    
]


