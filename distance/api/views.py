from distance.models import Distance
from serializers import DistanceSerializer
from paginations import DistancePagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@permission_classes((IsAuthenticatedOrReadOnly,))
class DistanceViewSet(viewsets.ModelViewSet):
    model = Distance
    serializer_class = DistanceSerializer
    pagination_class = DistancePagination
    queryset = Distance.objects.all()

    def retrieve(self, request, pk):
        queryset = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.id = %s', [pk])
        serializers = DistanceSerializer(queryset, many=True)
        return Response(serializers.data)
