from rest_framework import serializers
from .models import User,Address


class addressserializer(serializers.ModelSerializer):
    class Meta :
        model = Address
        fields = ('address_line1', 'address_line2', 'city', 'state')


class Userserializers(serializers.ModelSerializer):

   address = serializers.CharField(default=1)

   class Meta :
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')