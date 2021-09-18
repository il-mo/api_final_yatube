from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator, UniqueForYearValidator


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(),
    )

    class Meta:
        fields = '__all__'
        model = Follow
    #
    # def validate(self, request, attrs):
    #     if Follow.objects.filter(user=self.)
