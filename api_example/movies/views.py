from django.shortcuts import render
 
from rest_framework_mongoengine import viewsets as meviewsets
from api_example.movies.serializers import ToolSerializer
from api_example.movies.models import Tool
 
class ToolViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

# Create your views here.
