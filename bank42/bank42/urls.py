"""bank42 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from crawler import views

router = routers.DefaultRouter()
router.register('User', views.UserView, 'User')
router.register('Order', views.OrderView, 'Order')
router.register('AchvList', views.AchvListView, 'AchvList')
router.register('Achved', views.AchvedView, 'Achved')
router.register('Shop', views.ShopView, 'Shop')
router.register('Notice', views.NoticeView, 'Notice')

urlpatterns = [
    path('crawler/', include('crawler.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
