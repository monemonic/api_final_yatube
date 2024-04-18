from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

from .permissions import IsOwnerOrReadOnly, ReadOnly, IsUserOrReadOnly
from posts.models import Post, Follow, Group
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)


User = get_user_model()


class PermissionMixin(viewsets.ModelViewSet):
    """Миксин для permission."""

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return (ReadOnly(),)
        return super().get_permissions()


class PostViewSet(PermissionMixin):
    """API для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """API для групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionMixin):
    """API для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs["post_id"]),
        )


class FollowViewSet(viewsets.ModelViewSet):
    """API для подписок."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsUserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):

        try:
            following_username = self.request.data.get("following")
            follow = User.objects.get(username=following_username)
            if follow == self.request.user:
                raise ParseError
            serializer.save(
                user=self.request.user,
                following=follow
            )
        except:
            raise ParseError
