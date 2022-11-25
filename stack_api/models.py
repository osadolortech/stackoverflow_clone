from django.db import models
from user.models import User

# Create your models here.
class AskquestionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=150)
    ask_question = models.TextField(blank=False)
    tags = models.CharField(max_length=130)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    @property
    def number_of_comment(self):
        return Comment.objects.filter( post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_comment")
    post = models.ForeignKey(AskquestionModel,on_delete=models.CASCADE,related_name="question_comment")
    post_your_answer = models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_your_answer


class Reply_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("reply_comment"))
    user_coment = models.ForeignKey(Comment,on_delete=models.CASCADE,)
    post_reply =models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)


