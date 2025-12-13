from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import apartments_list, objects_list, blocks_list, apartments_create, objects_create, blocks_create, apartment_detail, object_detail, block_detail
from .class_api import ApartmentViewSet, ObjectViewSet

router = DefaultRouter()
router.register('apartments', ApartmentViewSet, basename='apartments')
router.register('objects', ObjectViewSet, basename='objects')


urlpatterns = [
    path('', include(router.urls))
    # path('apartments-list/', apartments_list, name='apartments-list'),
    # path('objects-list/', objects_list),
    # path('blocks-list', blocks_list, name="blocks-list"),
    # path('apartments-create/', apartments_create, name='apartments-create'),
    # path('objects-create/', objects_create, name="objects-create"),
    # path('blocks-create/', blocks_create, name="blocks-create"),
    # path('apartment-detail/<int:pk>', apartment_detail, name='apartment-detail'),
    # path('object-detail/<int:pk>', object_detail, name="object-detail"),
    # path('block-detail/<int:pk>', block_detail, name="block_detail")
]