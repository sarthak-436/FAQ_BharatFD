from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

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
    
    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', None) or self.question
    
    # Translate to different languages
    # For now, only Hindi and Bengali are taken
    
    def save(self, *args, **kwargs):
        translator = Translator()
        languages = ['hi', 'bn']
        
        for lang in languages:
            # Translate question if empty
            if not getattr(self, f'question_{lang}'):
                try:
                    translated_q = translator.translate(self.question, dest=lang).text
                    setattr(self, f'question_{lang}', translated_q)
                except:
                    pass
        
        super().save(*args, **kwargs)