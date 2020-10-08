from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import (
    AdminLevel0,
    AdminLevel1,
    AdminLevel2,
    AdminLevel3,
    AdminLevel4,
    AdminLevel5,
)


class AdminLevel0Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel0
        geo_field = "geometry"
        fields = "__all__"


class AdminLevel1Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel1
        geo_field = "geometry"
        fields = "__all__"


class AdminLevel2Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel2
        geo_field = "geometry"
        fields = "__all__"


class AdminLevel3Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel3
        geo_field = "geometry"
        fields = "__all__"


class AdminLevel4Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel4
        geo_field = "geometry"
        fields = "__all__"


class AdminLevel5Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminLevel5
        geo_field = "geometry"
        fields = "__all__"
