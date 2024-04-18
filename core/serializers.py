from rest_framework import serializers

from .models import Item, List


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "done", "url"]


class ListSerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ["id", "name", "owner", "url", "items"]
