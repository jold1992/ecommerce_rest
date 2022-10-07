from django.urls import path
from apps.products.api.views.general_views import MesureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView

urlpatterns = [
    path('mesure_unit/', MesureUnitListAPIView.as_view(), name='mesure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
]
