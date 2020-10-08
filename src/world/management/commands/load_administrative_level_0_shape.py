from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError

from world.models import AdminLevel0


class Command(BaseCommand):
    help = "Loads Administrative Level 0 Shape from https://www.geoboundaries.org/downloadFull.html#StandardizedCountry"

    def add_arguments(self, parser):
        parser.add_argument("shape_file", help="file must be in SHP format", type=str)

    def handle(self, *args, **options):
        admin_level_0_mapping = {
            "name": "shapeName",
            "iso_3166_alpha_3": "shapeISO",
            "geometry": "MULTIPOLYGON",
        }
        shape_file = options.get("shape_file")
        layer_mapping = LayerMapping(
            AdminLevel0, shape_file, admin_level_0_mapping, transform=False
        )
        layer_mapping.save(strict=True, verbose=True)
