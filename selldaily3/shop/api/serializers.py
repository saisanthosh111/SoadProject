from shop.models import Product,Orders,OrderProduct
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Product
        fields = ['product_name', 'category','subcategory','price','desc','image']

    def get_image_url(self, obj):
        return "http://localhost:8000"+obj.image.url

class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = [
            'pk'
        ]

class OrderSerializer(serializers.ModelSerializer):
    # items_json = OrderListSerializer(many=True)
    class Meta:
        model = Orders
        fields = ['items_json','name','amount','email','address','city','state','zip_code']


class OrderputSerializer(serializers.HyperlinkedModelSerializer):
    items_json = OrderListSerializer(many=True)
    class Meta:
        model = Orders
        fields = ['items_json','name','amount','email','address','city','state','zip_code']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_typr':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {
        'password':{'write_only':True}
        }
    def save(self):
        user = User(
        email = self.validated_data['email'],
        username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password!=password2:
            print(password,password2)
            raise serializers.ValidationError({'password':'passwords must match'})
        user.set_password(password)
        user.save()
        return user
    # def create(self, validated_data):
    #     """Create and return a new patient"""
    #
    #     patient = Orders(
    #         items_json=validated_data["items_json"],
    #         amount=validated_data["amount"],
    #         email=validated_data["email"],
    #         address=validated_data["address"],
    #         city=validated_data["city"],
    #         state=validated_data["state"],
    #         zip_code=validated_data["zip_code"]
    #     )
    #     patient.save()
    #     return patient
