from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name', 'password', 'contact_details', 'sex', 'course', 'user_type','is_verified', 'is_active']

    # def save(self, **kwargs):

    #     user_type = self.validated_data.get('user_type')  
    #     if user_type == 'Cashier':            
    #         user = User.objects.create_user(
    #             username=self.validated_data['username'],
    #             email=self.validated_data['email'],
    #             first_name=self.validated_data['first_name'],
    #             last_name=self.validated_data['last_name'],
    #             password=self.validated_data['password'],
    #             contact_details=self.validated_data['contact_details'],
    #             sex=self.validated_data['sex'],
    #             course=self.validated_data['course'],     
    #             user_type=self.validated_data['user_type'],    
    #         )

    #         user.is_active = False
    #         user.save()