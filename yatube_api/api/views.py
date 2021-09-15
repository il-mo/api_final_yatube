
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)



# TODO: дописать perform_create

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):

        group = get_object_or_404(Group, id=self.kwargs['group'])
        serializer.save(author=self.request.user, group=group)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, serializer):
        super().perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, serializer):
        super().perform_destroy(serializer)


class FollowViewSet(viewsets.ModelViewSet):

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        following = Follow.objects.all()
        queryset = following.filter(user=self.request.user)
        return queryset

