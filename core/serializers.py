from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Item, List


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "list", "done"]


class ListSerializer(WritableNestedModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ["id", "name", "owner", "items"]
