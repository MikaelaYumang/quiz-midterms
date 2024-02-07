from django.shortcuts import render
from rest_framework import status

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from appbackend.products import products

from .models import *
from .serializers import *
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

products = [
    {
      '_id': '1',
      'name': 'Airpods Wireless Bluetooth Headphones',
      'image': '/images/airpods.jpg',
      'description':
        'Bluetooth technology lets you connect it with compatible devices wirelessly High-quality AAC audio offers immersive listening experience Built-in microphone allows you to take calls while working',
      'brand': 'Apple',
      'category': 'Electronics',
      'price': 89.99,
      'countInStock': 0,
      'rating': 4.5,
      'numReviews': 12,
    },
    {
      '_id': '2',
      'name': 'iPhone 11 Pro 256GB Memory',
      'image': '/images/phone.jpg',
      'description':
        'Introducing the iPhone 11 Pro. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life',
      'brand': 'Apple',
      'category': 'Electronics',
      'price': 599.99,
      'countInStock': 7,
      'rating': 4.0,
      'numReviews': 8,
    },
    {
      '_id': '3',
      'name': 'Cannon EOS 80D DSLR Camera',
      'image': '/images/camera.jpg',
      'description':
        'Characterized by versatile imaging specs, the Canon EOS 80D further clarifies itself using a pair of robust focusing systems and an intuitive design',
      'brand': 'Cannon',
      'category': 'Electronics',
      'price': 929.99,
      'countInStock': 5,
      'rating': 3,
      'numReviews': 12,
    },
    {
      '_id': '4',
      'name': 'Sony Playstation 4 Pro White Version',
      'image': '/images/playstation.jpg',
      'description':
        'The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music',
      'brand': 'Sony',
      'category': 'Electronics',
      'price': 399.99,
      'countInStock': 11,
      'rating': 5,
      'numReviews': 12,
    },
    {
      '_id': '5',
      'name': 'Logitech G-Series Gaming Mouse',
      'image': '/images/mouse.jpg',
      'description':
        'Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. The six programmable buttons allow customization for a smooth playing experience',
      'brand': 'Logitech',
      'category': 'Electronics',
      'price': 49.99,
      'countInStock': 7,
      'rating': 3.5,
      'numReviews': 10,
    },
    {
      '_id': '6',
      'name': 'Amazon Echo Dot 3rd Generation',
      'image': '/images/alexa.jpg',
      'description':
        'Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small space',
      'brand': 'Amazon',
      'category': 'Electronics',
      'price': 29.99,
      'countInStock': 0,
      'rating': 4,
      'numReviews': 12,
    },
  ]
  

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request, pk=None):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request, pk=None):
    # products = Product.objects.all()
    if pk:
        # If a pk is provided, find and return the corresponding product
        for product in products:
            if product['_id'] == pk:
                return Response(product)
        # If no matching product is found, return a 404 Not Found response
        return Response({'error': 'Product not found'}, status=404)
    # serializer = ProductSerializer(products, many = True)
    # If no pk is provided, return the entire products list
    return Response(products)

@csrf_exempt
def saveShippingAddress(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data['user']
        address = data['address']
        city = data['city']
        postalCode = data['postalCode']
        country = data['country']

        user = User.objects.get(id=user_id)
        
        shipping_address, created = ShippingAddress.objects.update_or_create(
            user=user,
            defaults={
                'address': address,
                'city': city,
                'postalCode': postalCode,
                'country': country,
            },
        )

        return JsonResponse({'status': 'Address saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
