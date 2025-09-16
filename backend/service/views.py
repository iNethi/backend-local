from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for managing Service model.
    Read-only operations only - no authentication required.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
