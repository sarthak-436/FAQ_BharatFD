from django.shortcuts import render
from django.http import HttpResponse
from .models import FAQ

class FAQViewSet(viewsets.ModelViewSet):
    
    queryset = FAQ.objects.all()
    

