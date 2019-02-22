"""nearbyshops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from shops import views
from rest_framework import routers
from nearbyshops.api import viewset
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users',viewset.UserViewSet)
router.register(r'groups',viewset.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('',include(router.urls)),
    path('road',views.Road,name="road"),
    path('road/<int:id>',views.RoadUnit,name="roadunit"),
    path('hospital',views.Hospital.as_view(),name="hospital"),
    path('spa',TemplateView.as_view(template_name='index.html')),
    path('api/hospital/<str:lat>/<str:long>',viewset.HospitalViewSet.as_view({'get':'list'})),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework'))

]
