from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Unified Add to Cart (takes model type as str and object ID)
     path('add-to-cart/<str:model>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Update & Remove using Cart item ID instead of Product ID
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('refurbished/', views.refurbished_products, name='refurbished'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('refurbished/', views.refurbished_products, name='refurbished_products'),

]