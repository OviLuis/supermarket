# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(verbose_name='ID Cliente', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nombre del Cliente', max_length=191)),
                ('email', models.CharField(verbose_name='Email del producto', max_length=191)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CustomerProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID Pedido', primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(verbose_name='Cliente', db_column='customer_id', related_name='cp_customer', on_delete=django.db.models.deletion.PROTECT, to='products.Customer')),
            ],
            options={
                'verbose_name': 'Producto por Cliente',
                'verbose_name_plural': 'Productos por Cliente',
                'db_table': 'customer_product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(verbose_name='ID Producto', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nombre del producto', max_length=191)),
                ('product_description', models.CharField(verbose_name='Descripcion del producto', max_length=191)),
                ('price', models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='customerproduct',
            name='product_id',
            field=models.ForeignKey(verbose_name='Producto', db_column='product_id', related_name='cp_producto', on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]
