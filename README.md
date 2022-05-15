# supermarket
API que permite generar una order de pedidos de productos para un cliente, de acuerdo a los productos permitidos para el mismo. Esta construida en Django usando Django REST Framework


## Instalación
1. crear entorno virtual (opcional)
2. instalar las dependencias
```bash
pip install -r requirements.txt #ejecutar en la raiz del proyecto
```

3. ejecutar las migraciones del proyecto
```python
python manage.py makemigrations
python manage.py migrate
```
Al ejecutar las migraciones  se crean los datos por defecto para: Productos, Clientes, Productos por cliente. los datos estan registados en el archivo initial_data.json

## requerimientos
1. version de python >= 3.6


## Documentación API

**root**: http://localhost:8000/api/v1

* POST /orders/ : permite crear un nueva orden para un cliente:
## ejemplo
```json
{
       "customer_id": 1,
       "creation_date": "2022-05-14",
       "delivery_address": "Cra13",
       "total": "500.00",
       "detail": [
           {
               "product_id": 4,
               "product_description": "producto D",
               "price": "500.00",
               "quantity": 1
           }

       ]
   }
```
* GET /orders/: consulta todas las ordenes registradas
* GET /orders/customer/<customer_id>/?init_date=&end_date= : Obtiene todas las ordenes de un cliente en un rango de fechas. el parametro customer_id es el identificador del cliente al que se le quiere consultar las ordenes.
