from django.contrib.gis import admin
from .models import (
    AdminLevel0,
    AdminLevel1,
    AdminLevel2,
    AdminLevel3,
    AdminLevel4,
    AdminLevel5,
)

admin.site.register(AdminLevel0, admin.GeoModelAdmin)
admin.site.register(AdminLevel1, admin.GeoModelAdmin)
admin.site.register(AdminLevel2, admin.GeoModelAdmin)
admin.site.register(AdminLevel3, admin.GeoModelAdmin)
admin.site.register(AdminLevel4, admin.GeoModelAdmin)
admin.site.register(AdminLevel5, admin.GeoModelAdmin)
