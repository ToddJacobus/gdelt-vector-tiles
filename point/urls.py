from django.urls import path, include
from rest_framework.routers import DefaultRouter

from point import views


router = DefaultRouter()
router.register('point', views.PointViewSet)

app_name = 'point'

urlpatterns = [
    path('', include(router.urls)),
]
