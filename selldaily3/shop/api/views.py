from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from shop.models import Product,Orders
from .serializers import ProductSerializer,OrderSerializer,OrderputSerializer,RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(http_method_names=['GET',])
@permission_classes((IsAuthenticated,))
def Product_list_view_get(request):
    try:
        data = Product.objects.all()
        serializer = ProductSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=['GET',])
@permission_classes((IsAuthenticated,))
def Product_list_name_get(request,pk):
    try:
        data = Product.objects.filter(subcategory=pk)
        serializer = ProductSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['POST',])
@permission_classes((IsAuthenticated,))
def Order_list_view_post(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
@permission_classes((IsAuthenticated,))
def Order_detail_view_get(request, slug):
    try:
        data = Orders.objects.get(order_id=slug)
        user = request.user.username
        if data.name != user:
            return Response({'response':'you dont have authority to access this data'})

        serializer = OrderSerializer(data)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response']="successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data["token"]=token
        else:
            data = serializer.errors
        return Response(data)
