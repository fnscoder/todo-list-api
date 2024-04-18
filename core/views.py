from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import List
from .serializers import ListSerializer


class ListViewSet(ModelViewSet):
    """
    API endpoint that allows lists to be viewed or edited
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]
