from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserTrainList)
# router.register('count/', views.TrainsCountView)

urlpatterns = [
    path("", include(router.urls)),
]
