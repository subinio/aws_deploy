"""DBProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import BrightWay.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BrightWay.views.home, name = 'home'),
    path('select/', BrightWay.views.select, name = 'select'),
    path('select2/', BrightWay.views.select2, name = 'select2'),
    path('loginChild/', BrightWay.views.loginChild, name = 'loginChild'),
    path('loginParent/', BrightWay.views.loginParent, name = 'loginParent'),
    path('parentSignup/', BrightWay.views.parentSignup, name = 'parentSignup'),
    path('childSignup/', BrightWay.views.childSignup, name = 'childSignup'),
    path('logout/', BrightWay.views.logout, name = 'logout'),
    path('map/', BrightWay.views.map, name = 'map'),
    path('map2/', BrightWay.views.map2, name = 'map2'),
    path('childMypage/', BrightWay.views.childMypage, name = 'childMypage'),
    path('parentMypage/', BrightWay.views.parentMypage, name = 'parentMypage'),
]
