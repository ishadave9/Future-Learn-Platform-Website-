"""
URL configuration for FutureLearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.course,name='courses'),
    path('courses-form/',views.course_form,name='courses-form'),
    path('quiz/',views.quiz,name='quize'),
    path('contact/',views.contact,name='contact'),
    # path('login-signup/',views.login_signup,name='login-signup'),

    path('',views.user_register, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
