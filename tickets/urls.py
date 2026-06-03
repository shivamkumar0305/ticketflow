from django.urls import path,include
from .views import TicketsViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets',TicketsViewset, basename="ticket")


urlpatterns=[
    path('tic', include(router.urls))
    ]