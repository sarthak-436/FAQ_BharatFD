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
    html_content = """
    <html>
    <head><title>FAQ System</title></head>
    <body>
        <h1>FAQ System - Made by Sarthak</h1>
        <p>Welcome to the FAQ System. Here are the available API endpoints:</p>
        <ul>
            <li><strong>FAQ Admin:</strong> <a href="http://localhost:8000/admin">http://localhost:8000/admin</a></li>
            <li><strong>Fetch FAQs in English:</strong> <a href="http://localhost:8000/api/faqs/">http://localhost:8000/api/faqs/</a></li>
            <li><strong>Fetch FAQs in Hindi:</strong> <a href="http://localhost:8000/api/faqs/?lang=hi">http://localhost:8000/api/faqs/?lang=hi</a></li>
            <li><strong>Fetch FAQs in Bengali:</strong> <a href="http://localhost:8000/api/faqs/?lang=bn">http://localhost:8000/api/faqs/?lang=bn</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('faqs.urls')),
    path('', faq_home),
]
