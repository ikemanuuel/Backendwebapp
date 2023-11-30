from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes= [AllowAny]
    # def get_queryset(self):
    #     queryset = User.objects.all()

    #     return queryset

    def create (self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user_type = request.data.get('user_type')

        hashed_password = make_password(password)

        new_user = User.objects.create(
            username=username,
            password=hashed_password,
            email=email,
            user_type=user_type
        )

        return Response(UserSerializer(new_user).data, status=201)
    

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class FetchAccountRequest(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        # allowed_user_type = ['Cashier', 'Inventory Clerk', 'Inventory Sales']
        queryset = User.objects.filter(is_verified=False, user_type__in=['Cashier', 'Inventory Clerk', 'Inventory Sales'])
        return queryset
    
class FetchRegisteredAccount(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        # allowed_user_type = ['Cashier', 'Inventory Clerk', 'Inventory Sales']
        queryset = User.objects.filter(is_verified=True, user_type__in=['Cashier', 'Inventory Clerk', 'Inventory Sales'])
        return queryset


class AcceptAccountRequest(generics.UpdateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    def update (self, request, *args, **kwargs):
        instance = self.get_object()

        instance.is_verified = True
        instance.save()

        return Response({'message': 'success'})
    
class DeclineAccountRequest(generics.UpdateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    def update (self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({'message': 'success'})
    
class ActivateAccount(generics.UpdateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    def update (self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = True
        instance.save()

        return Response({'message': 'success'})

class DeactivateAccount(generics.UpdateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    def update (self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response({'message': 'success'})


