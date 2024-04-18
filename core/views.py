from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import List, Item
from .serializers import ListSerializer, ItemSerializer


class ListViewSet(ModelViewSet):
    """
    API endpoint that allows lists to be viewed or edited
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]


class ItemViewSet(ModelViewSet):
    """
    API endpoint that allows list items to be viewed or edited
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
