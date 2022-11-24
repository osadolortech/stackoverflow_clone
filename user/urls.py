from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProfileView


route = DefaultRouter()
route.register('profile', ProfileView)


urlpatterns = [
    path("",include(route.urls))
]