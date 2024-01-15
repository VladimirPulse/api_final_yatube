"""Модуль views."""
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnlyPermission
from posts.models import Group, Post
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Класс для публикаций."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создание нового поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс группы для публикаций."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class CommentViewSet(viewsets.ModelViewSet):
    """Класс viewset для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    )

    def get_post(self):
        """Проверка на существование и получение отдельного поста."""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        """Запрос на получение комментариев отдельного поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создание нового комментария."""
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Класс для подписчиков."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Переопределение запроса."""
        return self.request.user.follower.all()
