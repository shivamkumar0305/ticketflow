from django.shortcuts import render
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import TicketSerializer
from .models import Ticket
from accounts.models import User
from rest_framework.decorators import action





# Create your views here.
class TicketsViewset(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff :
            return Ticket.objects.all().order_by('-created_at')
        
        return Ticket.objects.filter(created_by=user).order_by('-created_at')
    
    @action(
        detail=True,
        methods=['patch'],
        url_path='assign',
        permission_classes =  [IsAuthenticated, IsAdminUser]
    )
    def assign_agent(self, request, pk=None):
        ticket = self.get_object()
        agent_id = request.data.get('agent')

        if not agent_id:
            return Response(
                {'error':'Agent ID is required.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        try:
            agent = User.objects.get(id=agent_id, is_staff=True)
        except User.DoesNotExist:
            return Response(
                {"error":"Assignment failed. provided id is not an agent id"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        ticket.assigned_to = agent
        ticket.save()

        serializer = self.get_serializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


