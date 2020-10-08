from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError

from world.models import AdminLevel2


class Command(BaseCommand):
    help = "Loads Administrative Level 2 Shape from https://www.geoboundaries.org/downloadFull.html#StandardizedCountry"

    def add_arguments(self, parser):
        parser.add_argument("shape_file", help="file must be in SHP format", type=str)

    def handle(self, *args, **options):
        admin_level_2_mapping = {
            "name": "shapeName",
            "iso": "shapeISO",
            "geometry": "MULTIPOLYGON",
        }
        shape_file = options.get("shape_file")
        layer_mapping = LayerMapping(
            AdminLevel2, shape_file, admin_level_2_mapping, transform=False
        )
        layer_mapping.save(strict=True, verbose=True)
