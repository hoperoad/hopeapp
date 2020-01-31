"""hopeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from hopemapapp.models import Customer, HopeEmployee
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'lat', 'lng')

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# hope_employee
class HopeEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HopeEmployee
        fields = ('user_id', 'password', 'first_name', 'last_name', 'work_address', 'email', 'lat', 'lon')

class HopeEmployeeViewSet(viewsets.ModelViewSet):
    queryset = HopeEmployee.objects.all()
    serializer_class = HopeEmployeeSerializer

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'hopeemployee', HopeEmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hopemapapp/', include('hopemapapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hopemapapp/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
