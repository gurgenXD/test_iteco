from rest_framework import serializers

from app.models import RollingStock, Product, RollingStockProducts


class RollingStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingStock
        fields = ["id", "rolling_stock_type", "max_capacity"]


class ProductSerializer(serializers.ModelSerializer):
    p_type = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "p_type", "weight"]

    def get_p_type(self, obj):
        return obj.get_p_type_display()


class RollingStockProductsReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RollingStockProducts
        fields = ["id", "product"]


class RollingStockProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollingStockProducts
        fields = ["id", "rolling_stock", "product"]

    def validate(self, data):
        product = data["product"]
        rolling_stock = data["rolling_stock"]

        if product.p_type not in rolling_stock.rolling_stock_type.product_types:
            raise serializers.ValidationError(
                "Тип продукции не соответсвует требованиям."
            )

        if (
            product.weight < rolling_stock.rolling_stock_type.min_weight
            or product.weight > rolling_stock.rolling_stock_type.max_weight
        ):
            raise serializers.ValidationError(
                "Масса единицы металла не соответсвует требованиям."
            )

        if (
            self.Meta.model.objects.filter(rolling_stock=rolling_stock).count()
            >= rolling_stock.rolling_stock_type.max_count
        ):
            raise serializers.ValidationError(
                "Превышено максимальное колличество продукции в подвижном составе."
            )

        total_weight = sum(
            self.Meta.model.objects.filter(rolling_stock=rolling_stock).values_list(
                "product__weight", flat=True
            )
        )

        if rolling_stock.max_capacity < total_weight + product.weight:
            raise serializers.ValidationError("Масса не соответсвует требованиям.")

        return data
