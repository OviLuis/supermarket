from django.db import models


class Order(models.Model):

    order_id = models.AutoField(primary_key=True, verbose_name="ID Pedido")
    customer_id = models.ForeignKey('products.Customer', db_column='customer_id', related_name='order_customer',
                                    on_delete=models.PROTECT, verbose_name='Cliente')
    creation_date = models.DateField(auto_now_add=True, editable=False, verbose_name='Fecha de Creacion')
    delivery_address = models.CharField(max_length=191, verbose_name='Direccion entrega')
    total = models.DecimalField(verbose_name='Total', max_digits=15, decimal_places=2)

    def __str__(self):
        return '%d' % self.order_id

    class Meta:
        managed = True
        db_table = 'order'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True, verbose_name="ID Detalle Pedido")
    order_id = models.ForeignKey('Order', db_column='order_id', related_name='detail',
                                 on_delete=models.PROTECT, verbose_name='Orden')
    product_id = models.ForeignKey('products.Product', db_column='customer_id', related_name='order_detail_product',
                                   on_delete=models.PROTECT, verbose_name='Producto')
    product_description = models.CharField(max_length=191, verbose_name='Descripcion del producto')
    price = models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return '%d' % self.order_detail_id

    class Meta:
        managed = True
        db_table = 'order_detail'
        verbose_name = 'Detalle del pedido'
        verbose_name_plural = 'Detalles de los pedidos'