"""Модуль сериалайзеров."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для публикаций."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Тонкая настойка класса."""

        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер для группы публикаций."""

    class Meta:
        """Тонкая настойка класса."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментарией."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Класс тонкой настройки."""

        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для подписчиков."""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
        required=True
    )

    class Meta:
        """Класс тонкой настройки."""

        fields = "__all__"
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        """Проверка невозможности подписаться на себя."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Пользователь не может подписаться на себя!')
        return data
