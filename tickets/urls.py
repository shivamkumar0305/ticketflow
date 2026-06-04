from django.urls import path,include
from .views import TicketsViewset
from comments.views import CommentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets',TicketsViewset, basename="ticket")

comment_list = CommentViewSet.as_view({
    'get':'list',
    'post':'create'
    })


urlpatterns=[
    path('', include(router.urls)),
    path('tickets/<int:ticket_id>/comments/',comment_list, name='ticket-comment-list')
    ]