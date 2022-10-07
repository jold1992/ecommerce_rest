from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MesureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer    

class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer