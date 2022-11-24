from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CommentView,AskViews

route = DefaultRouter()
route.register("ask_question", AskViews)
route.register("comment", CommentView)

urlpatterns = [
    path("",include(route.urls))
]