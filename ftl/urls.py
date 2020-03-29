"""ftl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from myapp.views import send_json,index
from myapp import views
import populate_script
from rest_framework import routers
from myapp import views
router = routers.DefaultRouter()
router.register(r'users', views.userViewSet)
router.register(r'activity_periods', views.activity_periodsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendjson/', send_json),
    path('index', views.index),
    path('', include(router.urls)),
    path('showhome',views.show),
]

