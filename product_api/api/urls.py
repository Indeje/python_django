from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.apiOverview, name='apiOverview'),
	path('product-list/', views.showAll, name='product-list'),
	path('product-details/<int:pk>/', views.viewProduct, name='product-details'),
	path('product-create/', views.createProduct, name='product-create'),
	path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
	path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),
]
