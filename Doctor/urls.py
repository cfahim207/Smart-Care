from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewset,DesignationViewset,SpecilizationViewset,AvailableTimeViewset,ReviewViewset

router = DefaultRouter()

router.register('list', DoctorViewset,)
router.register('designation', DesignationViewset,)
router.register('specilization', SpecilizationViewset,)
router.register('available_time', AvailableTimeViewset,)
router.register('review', ReviewViewset,)

urlpatterns = [
    path('', include(router.urls)),
]