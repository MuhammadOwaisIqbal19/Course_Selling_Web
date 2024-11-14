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
from django.conf import settings
from django.conf.urls.static import static
from main import urls as main_app_urls
from course_details import urls as course_details_urls
from course_instructor import urls as course_instructor_urls
from django.contrib.auth.views import LoginView
from course_instructor.views import CustomLoginView  # Import the custom login view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main_app_urls)),
    path('',include(course_instructor_urls)),
    path('',include(course_details_urls)),

    path('registration/login/', CustomLoginView.as_view(), name='login'),  # Use your custom login view
    path('registration/', include('django.contrib.auth.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)