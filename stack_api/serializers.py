from rest_framework import serializers
from .models import AskquestionModel,Comment,Reply_Comment



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Comment
        fields =[
            "user","post","post_your_answer","created_at"
        ]

class Replyserializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Reply_Comment
        fields=[
            "user","user_coment","post_reply","created_at"
        ]


class AskquestinSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    comment = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = AskquestionModel
        fields = [
            "user","title","ask_question","tags","number_of_comment","comment","created_at"
        ]

