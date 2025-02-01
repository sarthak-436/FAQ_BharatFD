"""
URL configuration for FAQ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse
from rest_framework import routers
from faqs import views

router = routers.DefaultRouter()
router.register(r'faqs', views.FAQViewSet)

# Home Page 
def faq_home(request):
    html_content = """<html><head><title>FAQ System</title></head>
    <body><h1>FAQ System - Made by Sarthak</h1></body></html>"""
    return HttpResponse(html_content)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('faqs.urls')),
    path('', faq_home),
]
