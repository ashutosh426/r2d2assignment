from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from api_example.movies.views import ToolViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'mongo', ToolViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls