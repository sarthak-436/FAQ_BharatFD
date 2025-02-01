from rest_framework import serializers
from .models import FAQ

# To convert complex data types to python data types that can be easily rendered into JSON
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        lang = self.context.get('lang', 'en')
        
        data['question'] = instance.get_translated_question(lang)
        data['answer'] = instance.get_translated_answer(lang)
        
        return data