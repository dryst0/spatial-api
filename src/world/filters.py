from django.contrib.gis.db import models as geo_models
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter

from .models import (
    AdminLevel0,
    AdminLevel1,
    AdminLevel2,
    AdminLevel3,
    AdminLevel4,
    AdminLevel5,
)


class AdminLevel0Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel0
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }


class AdminLevel1Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel1
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }


class AdminLevel2Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel2
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }


class AdminLevel3Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel3
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }


class AdminLevel4Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel4
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }


class AdminLevel5Filter(GeoFilterSet):
    class Meta:
        model = AdminLevel5
        fields = ["geometry"]
        filter_overrides = {
            geo_models.MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {"lookup_expr": "covers"},
            }
        }
