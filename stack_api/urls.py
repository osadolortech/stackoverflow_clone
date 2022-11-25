from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CommentView,AskViews,Rplyview

route = DefaultRouter()
route.register("ask_question", AskViews)
route.register("comment", CommentView)
route.register("reply",Rplyview)

urlpatterns = [
    path("",include(route.urls))
]