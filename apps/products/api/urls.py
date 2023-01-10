from django.urls import path

from apps.products.api.views.general_views import MesureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_viewssets import (
                ProductListCreateAPIView, 
                ProductRetrieveUpdateDestroyAPIView
    )

urlpatterns = [
    path('mesure_unit/', MesureUnitListAPIView.as_view(), name='mesure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),   
]
