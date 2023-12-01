"""
URL configuration for mycan project.

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
from django.urls import path
from myapp3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wap/',views.wap),
    path('load1/',views.load1),
    path('load2/',views.load2),
    path('load3/',views.load3),
    path('load4/',views.load4),
    path('load5/',views.load5),
    path('load6/',views.load6),
    path('load7/',views.load7),
    path('load8/',views.load8),
    path('get/',views.get),
    path('create/',views.create),
    path('home/',views.home),
    path('contact/',views.contact),
    path('complain/',views.complain),
    path('product/',views.product),
]
