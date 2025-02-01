from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    # Default language (English)
    question = models.TextField()
    answer = RichTextField()

    # Translations (Hindi and Bengali)
    question_hi = models.TextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    answer_bn = RichTextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)