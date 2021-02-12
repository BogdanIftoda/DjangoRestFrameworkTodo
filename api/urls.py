from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserList, UserDetail
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserList.as_view(), name='userList'), 
    path('users/<int:pk>', UserDetail.as_view(), name='userDetail'),
]