# Generated by Django 3.2 on 2021-04-30 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_type', models.CharField(choices=[('r', 'Рулон'), ('s', 'Лист')], max_length=1, verbose_name='Тип продукции')),
                ('weight', models.PositiveIntegerField(verbose_name='Масса')),
            ],
            options={
                'verbose_name': 'Единица металла',
                'verbose_name_plural': 'Вся продукция',
            },
        ),
        migrations.CreateModel(
            name='RollingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_capacity', models.PositiveIntegerField(verbose_name='Максимальная грузоподъемность')),
            ],
            options={
                'verbose_name': 'Подвижной состав',
                'verbose_name_plural': 'Подвижные составы',
            },
        ),
        migrations.CreateModel(
            name='RollingStockType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_weight', models.PositiveIntegerField(verbose_name='Минимальная масса единицы металла')),
                ('max_weight', models.PositiveIntegerField(verbose_name='Максимальная масса единицы металла')),
                ('max_count', models.PositiveIntegerField(verbose_name='Максимальное количество единиц металла')),
                ('product_types', models.CharField(max_length=2, verbose_name='Типы продукции')),
            ],
            options={
                'verbose_name': 'Тип подвижного состава',
                'verbose_name_plural': 'Типы подвижных составов',
            },
        ),
        migrations.CreateModel(
            name='RollingStockProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolling_stock_products', to='app.product', verbose_name='Единица металла')),
                ('rolling_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolling_stock_products', to='app.rollingstock', verbose_name='Подвижной состав')),
            ],
            options={
                'verbose_name': 'Единица металла в подвижном составе.',
                'verbose_name_plural': 'Продукция в подвижном составе.',
            },
        ),
        migrations.AddField(
            model_name='rollingstock',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='rolling_stocks', through='app.RollingStockProducts', to='app.Product', verbose_name='Единицы металла'),
        ),
        migrations.AddField(
            model_name='rollingstock',
            name='rolling_stock_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolling_stocks', to='app.rollingstocktype', verbose_name='Тип подвижного состава'),
        ),
    ]
