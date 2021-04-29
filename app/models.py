from django.db import models


class RollingStockType(models.Model):
    """Тип подвижного состава."""

    min_weight = models.PositiveIntegerField("Минимальная масса единицы металла")
    max_weight = models.PositiveIntegerField("Максимальная масса единицы металла")
    max_count = models.PositiveIntegerField("Максимальное количество единиц металла")
    product_types = models.ManyToManyField(
        "ProductType", verbose_name="Типы продукции", related_name="rollin_stock_types"
    )

    class Meta:
        verbose_name = "Тип подвижного состава"
        verbose_name_plural = "Типы подвижных составов"

    def __str__(self):
        return str(id)


class RollingStock(models.Model):
    """Подвижной состав."""

    rolling_stock_type = models.ForeignKey(
        "RollingStockType",
        on_delete=models.CASCADE,
        verbose_name="Тип подвижного состава",
        related_name="rolling_stocks",
    )
    max_capacity = models.PositiveIntegerField("Максимальная грузоподъемность")

    class Meta:
        verbose_name = "Подвижной состав"
        verbose_name_plural = "Подвижные составы"

    def __str__(self):
        return str(id)


class ProductType(models.Model):
    """Тип продукции."""

    title = models.CharField("Название")

    class Meta:
        verbose_name = "Тип продукции"
        verbose_name_plural = "Типы продукции"

    def __str__(self):
        return str(id)


class Product(models.Model):
    """Единица металла (продукция)."""

    type_ = models.ForeignKey(
        "ProductType",
        on_delete=models.CASCADE,
        verbose_name="Тип продукции",
        related_name="products",
    )

    class Meta:
        verbose_name = "Единица металла"
        verbose_name_plural = "Вся Продукция"

    def __str__(self):
        return str(id)
