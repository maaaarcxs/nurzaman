from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import logout
from .serializers import LoginSerializer, RegisterSerializer, ProfileSerializer, FunctionChangePasswordSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@permission_classes([AllowAny])
def custom_login(request):
    serializers = LoginSerializer(data=request.data)
    serializers.is_valid(raise_exception=True)
    return Response(serializers.validated_data)


@api_view(["POST"])
def custom_register(request):
    serializers = RegisterSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def custom_logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({"detail": "Successfully logged out"})


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == "GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    if request.method in ["PUT", "PATCH"]:
        serializer = ProfileSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = FunctionChangePasswordSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"detail": "Password change successfully."})