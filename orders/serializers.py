
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import serializers

from orders.models import Order, OrderDetail
from products.models import Customer, Product, CustomerProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'customer_id', 'creation_date', 'delivery_address', 'total',)


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ('order_detail_id', 'product_id', 'product_description', 'price', 'quantity',)


class OrderSerializerv2(serializers.ModelSerializer):
    detail = OrderDetailSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ('order_id', 'customer_id', 'creation_date', 'delivery_address', 'total', 'detail')

    def validate(self, data):
        """
        Validar que la orden contenta maximo 5 productos por cliente.
        Adicionalmente, validar que los productos de la orden esten permitidos
        para el cliente
        :param attrs:
        :return:
        """

        products = data.get('detail')

        customer = data.get('customer_id')

        if products:
            # Validar que los producto ingresados en la orden sean los permitidos para el cliente
            # 1. Obtener los productos permitidos por cliente
            allow_products = CustomerProduct.objects.filter(customer_id=customer).values_list('product_id', flat=True)

            # 2. obtener el listado de los productos en la orden
            products_in_order = [p.get('product_id').pk for p in products]

            # 3. Encontrar la interseccion entre los dos conjuntos: productos permitivos y productos en la orden
            diff = Product.objects.filter(pk__in=products_in_order).exclude(pk__in=allow_products).values_list('product_description', flat=True)

            # 4. validar si existen elementos intersectados
            if diff:
                raise serializers.ValidationError('los siguientes productos no estan permitidos para este cliente: {}'.format(diff))

            # validar el numero de productos permitidos
            if len(products) > 5:
                raise serializers.ValidationError('El número maximo de productos permtidos es 5')

            # validar la cantidad permitida por cada producto
            quantity_by_product = [p for p in products if p.get('quantity') > 5]

            if quantity_by_product:
                raise serializers.ValidationError('Las unidadades permitidas por producto es 5')

        return data

    def create(self, validated_data):
        order_detail_data = validated_data.pop('detail')
        order = Order.objects.create(**validated_data)
        for product_data in order_detail_data:
            OrderDetail.objects.create(order_id=order, **product_data)
        return order