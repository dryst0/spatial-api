from uuid import uuid4

from django.contrib.gis.db import models as geo_models


class AdminLevel0(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100, unique=True)
    iso_3166_alpha_3 = geo_models.CharField(max_length=3)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_0"

    def __str__(self):
        return f"{self.name}"


class AdminLevel1(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100)
    iso = geo_models.CharField(max_length=5, null=True)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_1"

    def __str__(self):
        return f"{self.name}"


class AdminLevel2(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100)
    iso = geo_models.CharField(max_length=5, null=True)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_2"

    def __str__(self):
        return f"{self.name}"


class AdminLevel3(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100)
    iso = geo_models.CharField(max_length=5, null=True)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_3"

    def __str__(self):
        return f"{self.name}"


class AdminLevel4(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100)
    iso = geo_models.CharField(max_length=5, null=True)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_4"

    def __str__(self):
        return f"{self.name}"


class AdminLevel5(geo_models.Model):
    uuid = geo_models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = geo_models.CharField(max_length=100)
    iso = geo_models.CharField(max_length=5, null=True)
    geometry = geo_models.MultiPolygonField(srid=4326, geography=True)

    class Meta:
        db_table = "admin_level_5"

    def __str__(self):
        return f"{self.name}"
