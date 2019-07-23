from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
     class Meta:
        fields = (
            'question_text',
            'pub_date',
        )
        model = Question
