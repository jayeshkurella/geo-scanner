"""
URL configuration for Geo_Scanner project.

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
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('post_visited_api',post_visited_details)
router.register('posthospitalproductdetails',post_hospital_product_details)
router.register('post_feedback_api',post_feedback_details)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('getloggerbyhospitalid/<int:id>/',getloggerbyhospitalid, name='hospital'),
    path('getloggerbyloggerid/<uuid:id>/',getloggerbyloggerid),
    path('updataloggerdetails/<uuid:id>/',putloggerdetails),
    path('gethospitalproductdetails/<uuid:id>/',gethospitalproductdetails),
]
