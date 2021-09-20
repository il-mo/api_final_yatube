from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )

    def validate(self, data):
        if self.context['request'].user == data.get('following'):
            raise ValidationError('О')
        return data

    class Meta:
        fields = '__all__'
        model = Follow

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(), fields=('following', 'user')
        )
    ]

# if 'following' not in self.request.data:
#     raise ValidationError('Отсутсвуют данные для подписки')
# if self.request.user.username == self.request.data['following']:
#     raise ValidationError('Нельзя подписаться на себя')
