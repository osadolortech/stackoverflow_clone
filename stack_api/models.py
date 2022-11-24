from django.db import models
from user.models import User

# Create your models here.
class AskquestionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ask_question")
    title = models.CharField(max_length=150)
    ask_question = models.TextField(blank=False)
    tags = models.CharField(max_length=130)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    @property
    def number_of_comment(self):
        return Comment.objects.filter(question=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_comment")
    ask_question = models.ForeignKey(AskquestionModel,on_delete=models.CASCADE,related_name="question_comment")
    post_your_answer = models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now=True)

