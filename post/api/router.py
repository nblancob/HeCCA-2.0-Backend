from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='post', basename='post',viewset=PostApiViewSet)
#router_posts.register(prefix='create_df',basename='create_df',viewset=PostApiViewSet)

