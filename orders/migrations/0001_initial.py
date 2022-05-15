# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(verbose_name='ID Pedido', primary_key=True, serialize=False)),
                ('creation_date', models.DateField(verbose_name='Fecha de Creacion', auto_now_add=True)),
                ('delivery_address', models.CharField(verbose_name='Direccion entrega', max_length=191)),
                ('total', models.DecimalField(verbose_name='Total', max_digits=15, decimal_places=2)),
                ('customer_id', models.ForeignKey(verbose_name='Cliente', db_column='customer_id', related_name='order_customer', on_delete=django.db.models.deletion.PROTECT, to='products.Customer')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.AutoField(verbose_name='ID Detalle Pedido', primary_key=True, serialize=False)),
                ('product_description', models.CharField(verbose_name='Descripcion del producto', max_length=191)),
                ('price', models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('order_id', models.ForeignKey(verbose_name='Orden', db_column='order_id', related_name='order_detail_order', on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
                ('product_id', models.ForeignKey(verbose_name='Producto', db_column='customer_id', related_name='order_detail_product', on_delete=django.db.models.deletion.PROTECT, to='products.Product')),
            ],
            options={
                'verbose_name': 'Detalle del pedido',
                'verbose_name_plural': 'Detalles de los pedidos',
                'db_table': 'order_detail',
                'managed': True,
            },
        ),
    ]
