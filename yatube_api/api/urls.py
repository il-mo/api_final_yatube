from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='post')
router.register('v1/groups', GroupViewSet, basename='group')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [path('', include(router.urls))]
