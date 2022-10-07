from django.urls import path

from apps.products.api.views.general_views import MesureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductDestroyAPIView

urlpatterns = [
    path('mesure_unit/', MesureUnitListAPIView.as_view(), name='mesure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('product/list/', ProductListAPIView.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
]
