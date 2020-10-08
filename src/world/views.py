from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.pagination import GeoJsonPagination
from .filters import (
    AdminLevel0Filter,
    AdminLevel1Filter,
    AdminLevel2Filter,
    AdminLevel3Filter,
    AdminLevel4Filter,
    AdminLevel5Filter,
)
from .models import (
    AdminLevel0,
    AdminLevel1,
    AdminLevel2,
    AdminLevel3,
    AdminLevel4,
    AdminLevel5,
)
from .serializers import (
    AdminLevel0Serializer,
    AdminLevel1Serializer,
    AdminLevel2Serializer,
    AdminLevel3Serializer,
    AdminLevel4Serializer,
    AdminLevel5Serializer,
)


class AdminLevel0ViewSet(ModelViewSet):
    queryset = AdminLevel0.objects.all()
    serializer_class = AdminLevel0Serializer
    filterset_class = AdminLevel0Filter


class AdminLevel1ViewSet(ModelViewSet):
    queryset = AdminLevel1.objects.all()
    serializer_class = AdminLevel1Serializer
    filterset_class = AdminLevel1Filter


class AdminLevel2ViewSet(ModelViewSet):
    queryset = AdminLevel2.objects.all()
    serializer_class = AdminLevel2Serializer
    filterset_class = AdminLevel2Filter


class AdminLevel3ViewSet(ModelViewSet):
    queryset = AdminLevel3.objects.all()
    serializer_class = AdminLevel3Serializer
    filterset_class = AdminLevel3Filter


class AdminLevel4ViewSet(ModelViewSet):
    queryset = AdminLevel4.objects.all()
    serializer_class = AdminLevel4Serializer
    filterset_class = AdminLevel4Filter


class AdminLevel5ViewSet(ModelViewSet):
    queryset = AdminLevel5.objects.all()
    serializer_class = AdminLevel5Serializer
    filterset_class = AdminLevel5Filter
