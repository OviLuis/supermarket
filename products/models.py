from django.db import models


class Product(models.Model):

    product_id = models.AutoField(primary_key=True, verbose_name="ID Producto")
    name = models.CharField(max_length=191, verbose_name='Nombre del producto')
    product_description = models.CharField(max_length=191, verbose_name='Descripcion del producto')
    price = models.DecimalField(verbose_name='Precio', max_digits=10, decimal_places=2)

    def __str__(self):
        return '%d' % self.product_id

    class Meta:
        managed = True
        db_table = 'product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Customer(models.Model):

    customer_id = models.AutoField(primary_key=True, verbose_name="ID Cliente")
    name = models.CharField(max_length=191, verbose_name='Nombre del Cliente')
    email = models.CharField(max_length=191, verbose_name='Email del producto')

    def __str__(self):
        return '%d' % self.customer_id

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class CustomerProduct(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID Pedido")
    customer_id = models.ForeignKey('Customer', db_column='customer_id', related_name='cp_customer',
                                    on_delete=models.PROTECT, verbose_name='Cliente')
    product_id = models.ForeignKey('Product', db_column='product_id', related_name='cp_producto',
                                   on_delete=models.PROTECT, verbose_name='Producto')

    def __str__(self):
        return '%d' % self.customer_id

    class Meta:
        managed = True
        db_table = 'customer_product'
        verbose_name = 'Producto por Cliente'
        verbose_name_plural = 'Productos por Cliente'
