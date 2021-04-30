from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import RollingStock, RollingStockProducts
from app.serializers import (
    RollingStockSerializer,
    RollingStockProductsSerializer,
    RollingStockProductsReadSerializer,
)


class RollingStockProductsViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RollingStockProductsSerializer
    queryset = RollingStockProducts.objects.select_related(
        "product", "rolling_stock"
    ).all()


class RollingStockViewSet(viewsets.GenericViewSet):
    serializer_class = RollingStockSerializer
    queryset = RollingStock.objects.all()

    @action(detail=True)
    def products(self, request, pk=None, url_path="products"):
        """Просмотр списка металла внутри подвижного состава."""

        items = RollingStockProducts.objects.filter(rolling_stock=pk)
        return Response(RollingStockProductsReadSerializer(items, many=True).data)
