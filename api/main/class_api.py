from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from main.models import Apartment, Object, Block
from .serializers import ApartmentSerializer, ObjectSerializer, ApartmentDetailSerializer, BlockDetailSerializer, ObjectDetailSerializer, ApartmentCreateUpdateSerializer, ApartmentListSerializer, ObjectListSerializer, BlockSerializer
from .paginations import StandardResultSetPagination
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultSetPagination
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = {'floor', 'area', 'block__name', 'block__object__name', 'type', 'rooms_count'}
    # filterset_fields = {
    #     'area': ['gte', 'lte'], #area__gte=50, area__lte=100
    #     'name': ['icontains'], #area__icontains=проспект
    # }
    
    def get_serializer_class(self):
        if self.action == "retireve":
            return ApartmentDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
    

class ObjectViewSet(ReadOnlyModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ObjectDetailSerializer
        return  super().get_serializer_class()
    

class BlockViewSet(ReadOnlyModelViewSet):
    queryset=Block.objects.all()
    serializer_class=BlockSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BlockDetailSerializer
        return super().get_serializer_class()