from rest_framework import viewsets
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.response import Response

class FAQViewSet(viewsets.ModelViewSet):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    def get_queryset(self):
        return FAQ.objects.all()

    # Handles the GET request
    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        
        # Check for cached data
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'lang': lang})
        
        cache.set(cache_key, serializer.data, timeout=3600)
        return Response(serializer.data)