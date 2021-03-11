from rest_framework import serializers
from .models import Category

class CategorySerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')