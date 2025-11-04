from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.institutes.views import InstituteViewSet, DepartmentViewSet
from apps.scheduler.views import TimeSlotViewSet, OccupancyViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)
router.register('departments', DepartmentViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register('occupancies', OccupancyViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
