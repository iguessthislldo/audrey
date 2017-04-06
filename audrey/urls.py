"""dothing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/ Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from tag.serializers import Tag_Serializer, Tagged_Object_Serializer
from tag.models import Tag, Tagged_Object
from task.models import Task
from task.serializers import Task_Serializer

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

class Tag_ViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = Tag_Serializer
router.register(r'tags', Tag_ViewSet)

class Tagged_Object_ViewSet(viewsets.ModelViewSet):
    queryset = Tagged_Object.objects.all()
    serializer_class = Tagged_Object_Serializer
router.register(r'tagged_objects', Tagged_Object_ViewSet)

class Task_ViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_Serializer
router.register(r'tasks', Task_ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
