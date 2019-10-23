"""tutorial URL Configuration

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
from django.urls import path , include
from quickstart import views as views
from rest_framework import routers 


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'arule', views.AruleViewSet)
router.register(r'customeremotion', views.CustomeremotionViewSet)

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', views.rest_framework.urls , name='rest_framework')
    #path('api-auth/', views.viewsets , name='rest_framework')
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

'''

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]







