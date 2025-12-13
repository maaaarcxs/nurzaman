# from rest_framework.generics import (GenericAPIView, CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView)
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from .serializers import BlockSerializer, ObjectSerializer, ApartmentSerializer
# from main.models import Apartment, Block, Object


# class ApartmentListView(ListAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     permission_classes = (AllowAny,)


# class ApartmentDetailView(RetrieveAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"


# class ApartmentCreate(CreateAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer


# class ApartmentUpdate(UpdateAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"


# class ApartmentDelete(DestroyAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     lookup_field = "pk"


# class BlockListView(ListAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     permission_classes = (AllowAny,)


# class BlockDetailView(RetrieveAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"


# class BlockCreate(CreateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer


# class BlockUpdate(UpdateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"


# class BlockDelete(DestroyAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer
#     lookup_field = "pk"


# class ObjectList(ListAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#     pagination_class = None

# class ObjectDetail(RetrieveAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#     lookup_field = "pk"

# class ObjectCreate(CreateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer

# class ObjectUpdate(UpdateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#     lookup_field = "pk"

# class ObjectDelete(DestroyAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#     lookup_field = "pk"
