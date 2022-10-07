from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)

    def delete(self, request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)