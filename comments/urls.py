from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'tickets', CommentViewSet, basename='comment')

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', include(router.urls)),
    path('tickets/<int:ticket_id>/comments/', comment_list, name='ticket-comment-list'),
]