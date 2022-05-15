import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from orders.models import Order, OrderDetail
from orders.serializers import OrderSerializerv2


class OrderList(APIView):
    """
    Lista todas las ordenes,  o crea una nueva
    """
    def get(self, request, format=None):
        """
        obtener el listado de ordernes registradas.

        :param request:
        :param format:
        :return:
        """
        orders = Order.objects.all()
        serializer = OrderSerializerv2(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializerv2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def orders_by_customer(request, customer_id):
    """
    Permite  obtener el listado de ordenes para un cliente
    en particular para un rango de fechas si son enviados los parametros:
    init_date, end_date.
    Si no se envian los parametros se obtienen todas las ordenes del cliente
    :param request:
    :param customer_id:
    :return:
    """
    orders = Order.objects.filter(customer_id__pk=customer_id)
    init_date = request.query_params.get('init_date')
    end_date = request.query_params.get('end_date')

    if init_date and end_date:
        try:
            init_date = datetime.datetime.strptime(init_date, '%Y-%m-%d')
        except Exception:
            data = {'detail': 'el formato del parametro init_date debe ser aaaa-mm-dd'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except Exception:
            data = {'detail': 'el formato del parametro end_date debe ser aaaa-mm-dd'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        orders = orders.filter(
            creation_date__gte=init_date,
            creation_date__lte=end_date,

        )

    order_list = []
    for order in orders:
        obj = {
            'creation_date': order.creation_date.strftime("%d-%m-%Y"),
            'order_id': order.pk,
            'total': order.total,
            'delivery_address': order.delivery_address,
            'products': []
        }
        order_detail = order.detail.all()

        product = ['{} x {}'.format(p.quantity, p.product_id.product_description) for p in order_detail]

        obj['products'] = product
        order_list.append(obj)

    return Response(data=order_list, status=status.HTTP_200_OK)