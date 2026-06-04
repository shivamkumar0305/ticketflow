from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields =['id','comment','created_by','created_at','ticket']
        read_only_fields = ['id','created_at','created_by','ticket']
    