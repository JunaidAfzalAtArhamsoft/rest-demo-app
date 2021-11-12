from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('persons', views.PeronViewSet)
# router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('persons/', views.PeronViewSet.as_view({'get': 'list'}), name='list_create_view'),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
