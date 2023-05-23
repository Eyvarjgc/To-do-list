from django.urls import URLPattern,include,path
from . import views 
from . import serializers
from rest_framework import routers


router = routers.DefaultRouter()

router.register('Task', views.TaskViewset, 'Tasks')


urlpatterns = router.urls

