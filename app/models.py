from django.db import models

from app.enums import ProductType


class RollingStockType(models.Model):
    """Тип подвижного состава."""

    min_weight = models.PositiveIntegerField("Минимальная масса единицы металла")
    max_weight = models.PositiveIntegerField("Максимальная масса единицы металла")
    max_count = models.PositiveIntegerField("Максимальное количество единиц металла")
    product_types = models.CharField("Типы продукции", max_length=2)

    class Meta:
        verbose_name = "Тип подвижного состава"
        verbose_name_plural = "Типы подвижных составов"

    def __str__(self):
        return f"{self.__class__} id={self.id}"


class Product(models.Model):
    """Единица металла (продукция)."""

    p_type = models.CharField(
        "Тип продукции", choices=ProductType.choices, max_length=1
    )
    weight = models.PositiveIntegerField("Масса")

    class Meta:
        verbose_name = "Единица металла"
        verbose_name_plural = "Вся продукция"

    def __str__(self):
        return f"{self.__class__} id={self.id}"


class RollingStock(models.Model):
    """Подвижной состав."""

    rolling_stock_type = models.ForeignKey(
        RollingStockType,
        on_delete=models.CASCADE,
        verbose_name="Тип подвижного состава",
        related_name="rolling_stocks",
    )
    max_capacity = models.PositiveIntegerField("Максимальная грузоподъемность")
    products = models.ManyToManyField(
        Product,
        related_name="rolling_stocks",
        verbose_name="Единицы металла",
        blank=True,
        through="RollingStockProducts",
    )

    class Meta:
        verbose_name = "Подвижной состав"
        verbose_name_plural = "Подвижные составы"

    def __str__(self):
        return f"{self.__class__} id={self.id}"


class RollingStockProducts(models.Model):
    """Продукция в подвижном составе."""

    rolling_stock = models.ForeignKey(
        RollingStock,
        on_delete=models.CASCADE,
        verbose_name="Подвижной состав",
        related_name="rolling_stock_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Единица металла",
        related_name="rolling_stock_products",
    )

    class Meta:
        verbose_name = "Единица металла в подвижном составе."
        verbose_name_plural = "Продукция в подвижном составе."

    def __str__(self):
        return f"{self.__class__} id={self.id}"
