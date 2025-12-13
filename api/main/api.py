from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ApartmentSerializer, ObjectSerializer, BlockSerializer
from main.models import Apartment, Object, Block


@api_view(['GET'])
def objects_list(request):
    objects = Object.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(objects, request)
    serializer = ObjectSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def objects_create(request):
    serializer = ObjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def object_detail(request, pk):
    try:
        object = Object.objects.get(pk=pk)
    except Object.DoesNotExist:
        return Response({'detail': 'Not found'})
    
    if request.method == "GET":
        serializer = ObjectSerializer(object, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ObjectSerializer(object, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)
    
    if request.method == "DELETE":
        object.delete()
        return Response(status=204)
    

@api_view(['GET'])
def blocks_list(request):
    blocks = Block.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(blocks, request)
    serializer = BlockSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
    # serializer = BlockSerializer(blocks, many=True)
    # return Response(serializer.data)


@api_view(['POST'])
def blocks_create(request):
    serializer = BlockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def block_detail(request, pk):
    try:
        block = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return Response({"detail":"Not found"})
    
    if request.method == "GET":
        serializer = BlockSerializer(block, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = BlockSerializer(block, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        block.delete()
        return Response(status=204)


@api_view(['GET'])
def apartments_list(request):
    apartments = Apartment.objects.all()

    pagiantor = PageNumberPagination()
    pagiantor.page_size = 12

    result_page = pagiantor.paginate_queryset(apartments, request)
    serializer = ApartmentSerializer(result_page, many=True)

    return pagiantor.get_paginated_response(serializer.data)
    serializer = ApartmentSerializer(apartments, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def apartments_create(request):
    serializer = ApartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def apartment_detail(request, pk):
    try:
        apartment = Apartment.objects.get(pk=pk)
    except Apartment.DoesNotExist:
        return Response({"detail": "Not found"})
    
    if request.method == "GET":
        serializer = ApartmentSerializer(apartment, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ApartmentSerializer(apartment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        apartment.delete()
        return Response(status=204)
    