from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name ="products"),

    path('products/<str:pk>/', views.getProducts, name="product"),
    path('save-shipping/', views.saveShippingAddress, name='save-shipping'),


    # path('products/create/', views.createProduct, name='create_product'),
    # path('products/upload/', views.uploadProduct, name='upload_product'),
    # path('products/<int:pk>/reviews/', views.productReviews, name='product_reviews'),
    # path('products/top/', views.topProducts, name='top_products'),
    # path('products/<int:pk>/', views.productDetail, name='product_detail'),
    # path('products/delete/<int:pk>/', views.deleteProduct, name='delete_product'),
    # path('products/update/<int:pk>/', views.updateProduct, name='update_product'),




]