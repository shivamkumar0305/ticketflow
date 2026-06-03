from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Ticket
        fields = ['title','description','status','priority','created_by','assigned_to','created_at','updated_at']
        read_only_fields = ['status','created_by','assigned_to','created_at','updated_at']

        def validate(self,attrs):
            if self.instance:
                for field in attrs.keys():
                    if field!= 'description':
                        raise serializers.ValidationError({
                            field : "you are only allowed to change description"
                        })
            return attrs
        
