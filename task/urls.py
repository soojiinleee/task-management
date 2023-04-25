from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubTaskViewSet

router = DefaultRouter()
router.register("", TaskViewSet, basename="task")
router.register("subtask", SubTaskViewSet, basename="subtask")

urlpatterns = [
    path("", include(router.urls)),
]
