from django.shortcuts import render
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TicketSerializer
from .models import Ticket




# Create your views here.
class TicketsViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user

        if user.is_staff :
            return Ticket.objects.all().order_by('-created_at')
        
        return Ticket.objects.filter(created_by=user).order_by('-created_at')
    
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


