"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from mysite.views import hello, my_homepage_view, current_datetime, hours_ahead
from books.views import search_form, search

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^hello/$', hello),
    re_path(r'^$', my_homepage_view),
    path('time/', current_datetime),
    re_path(r'^time/plus/(\d{1,2})/$', hours_ahead),
    path('another_time_page/', current_datetime),
    re_path(r'^search_form/$', search_form),
    re_path(r'^search/$', search)
]
