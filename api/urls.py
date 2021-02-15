from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TaskViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', TaskViewSet, basename='tasks')

urlpatterns = router.urls
