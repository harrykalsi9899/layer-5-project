from django.shortcuts import render
from .serializers import Userserializers,addressserializer
from rest_framework import viewsets
from .models import User,Address
from rest_framework import generics
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = addressserializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        address_line1 = request.data.get('address_line1')
        address_line2 = request.data.get('address_line2')
        city = request.data.get('city')
        state = request.data.get('state')

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)

        address = Address.objects.create(address_line1=address_line1,address_line2=address_line2,city=city,
                                         state=state)

        user.address = address
        user.save()
        return Response({"data": Userserializers(user).data, "status": "Request Successful"})