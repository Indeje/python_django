from django.shortcuts import render, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Product List': '/product-list/',
		'Detail View': '/product-details/<int:pk>',
		'Create Product': '/product-create/',
		'Update Product': '/product-update/<int:pk>',
		'Delete Product': 'product-delete/<int:pk>',
	}

	return Response(api_urls)


@api_view(['GET'])
def showAll(request):
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(product, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=product, data=request.data, many=False)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
	try:
		product = Product.objects.get(id=pk)
		product.delete()

		return Response(f'Product {pk} deleted successfully!')

	except Exception as e:
		return HttpResponse(e)
