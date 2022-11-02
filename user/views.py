from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ProfileView(ModelViewSet):
    queryset = Profile.objects.select_related('user')
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)