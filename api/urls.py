from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TaskViewSet, UserViewSet, GroupViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('groups', GroupViewSet, basename='groups')
router.register('', TaskViewSet, basename='tasks')

urlpatterns = router.urls
