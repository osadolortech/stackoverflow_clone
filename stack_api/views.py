from rest_framework import viewsets
from .models import AskquestionModel,Comment,Reply_Comment
from .userpermission import CustomPermission
from .serializers import AskquestinSerializer,CommentSerializer,Replyserializer

# Create your views here.

class AskViews(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    queryset = AskquestionModel.objects.all()
    serializer_class = AskquestinSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class Rplyview(viewsets.ModelViewSet):
    queryset = Reply_Comment.objects.all()
    serializer_class = Replyserializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)