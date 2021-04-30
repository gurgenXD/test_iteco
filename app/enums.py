from django.db.models import TextChoices


class ProductType(TextChoices):
    ROLL = "r", "Рулон"
    SHEET = "s", "Лист"
