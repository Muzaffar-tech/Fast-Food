from rest_framework import serializers
from .models import Category, Item, Order

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'price', 'category']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        view_name='item-detail',
        queryset=Item.objects.all()
    )

    class Meta:
        model = Order
        fields = ['url', 'id', 'item', 'quantity', 'order_date']
