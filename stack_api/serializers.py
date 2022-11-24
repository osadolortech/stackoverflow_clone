from rest_framework import serializers
from .models import AskquestionModel,Comment




class AskquestinSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = AskquestionModel
        fields = [
            "user","title","ask_question","tags","created_at"
        ]

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.user.username")
    class Meta:
        model = Comment
        fields =[
            "user","ask_question","post_your_answer","created_at"
        ]
