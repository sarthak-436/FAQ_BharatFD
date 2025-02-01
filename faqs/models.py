from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.utils.html import strip_tags

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

    def get_translated_answer(self, lang): 
        return getattr(self, f'answer_{lang}', None) or self.answer

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

            # Translate answer if empty
            if not getattr(self, f'answer_{lang}') and self.answer:
                try:
                    translated_a = translator.translate(
                        strip_tags(self.answer),  # Remove HTML for translation
                        dest=lang
                    ).text
                    setattr(self, f'answer_{lang}', translated_a)
                except:
                    pass

        super().save(*args, **kwargs)