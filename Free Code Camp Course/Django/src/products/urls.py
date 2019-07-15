from django.urls import path
from .views import (
    dynamic_lookup_view,
    product_create_view,
    product_create_view2,
    product_create_view3,
    product_delete_view,
    product_detail_view,
    product_list_view
)

app_name = 'products'
urlpatterns = [
    #path('', product_detail_view),
    path('create/', product_create_view),
    path('create2/', product_create_view2),
    path('create3/', product_create_view3),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='products-list'),
]
