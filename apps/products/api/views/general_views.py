from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MesureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer    

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer