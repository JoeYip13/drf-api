from rest_framework import generics, permissions
from drf_api.permissions import isOwnerOrReadOnly
from .models import Likes
from .serializers import LikesSerializer


class LikesList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
