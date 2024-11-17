from django.contrib import admin
from django.urls import path, include
from .views import if_is_instructor, main_page, course_detail
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", if_is_instructor, name='main'),
    path("main_page/", main_page, name='main_page'),
    path("course/<int:course_id>/", course_detail, name='course_detail'),
    path('registration/login/', auth_views.LoginView.as_view(), name='login'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
