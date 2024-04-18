from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v_1 = DefaultRouter()
router_v_1.register("posts", PostViewSet, basename="v1_posts")
router_v_1.register("groups", GroupViewSet, basename="v1_groups")
router_v_1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="v1_comments"
)
router_v_1.register("follow", FollowViewSet, basename="v1_follow")


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path("v1/", include(router_v_1.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
