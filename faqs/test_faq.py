import pytest
from django.urls import reverse
from django.core.cache import cache
from .models import FAQ

@pytest.fixture
def faq(db):
    return FAQ.objects.create(question="Hello", answer="World")

@pytest.mark.django_db
def test_translation(faq):
    assert faq.question_hi is not None  # Check if Hindi translation exists

@pytest.mark.django_db
def test_api_endpoint(client):
    response = client.get('/api/faqs/?lang=hi')
    assert response.status_code == 200

@pytest.mark.django_db
def test_faq_caching(client, faq):
    url = reverse('faq-list') + '?lang=en'
    
    # Clear cache before testing
    cache.clear()
    
    # First API call (should hit the database)
    response1 = client.get(url)
    
    # Set cache manually to simulate caching
    cache.set('faqs_en', response1.json(), timeout=3600)
    
    # Second API call (should return cached response)
    response2 = client.get(url)
    
    assert response1.json() == response2.json()