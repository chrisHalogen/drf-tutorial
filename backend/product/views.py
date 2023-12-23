from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import status
from .models import  Product
from .serializers import ProductSerializer
from rest_framework import viewsets

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@api_view()
def product_index(request):
    return Response({'message':'This is the Product Base url'})

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # product_data = [{
        #     'id' : product.id,
        #     'name' : product.name,
        #     'description' : product.description,
        #     'price' : product.price,
        #     'quantity' : product.quantity
        # } for product in products]

        # data = []
        # for product in products:
        #     temp = {
        #             'id' : product.id,
        #             'description' : product.description,
        #             'price' : product.price,
        #             'quantity' : product.quantity
        #         }
        #     data.append(temp)

        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # data = request.data
        # product = Product(
        #     name=data['name'],
        #     description=data['description'],
        #     price=data['price'],
        #     quantity=data['quantity'],
        # )

        # product.save()

        # output = {
        #     'message' : 'Product Created Successfully',
        #     'new_id' : product.id
        # }

        # return Response(output, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # data = request.data
        # product.name = data['name']
        # product.description = data['description']
        # product.price = data['price']
        # product.quantity = data['quantity']
        # product.save()

        # output = {
        #     'message' : 'Product Updated Successfully',
        #     'product_id' : product.id
        # }

        # return Response(output, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

