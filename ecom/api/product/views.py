from rest_framework import viewsets
from .models import Product
from .serialize import ProductSerialzer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerialzer