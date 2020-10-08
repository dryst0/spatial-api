from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import (
    AdminLevel0ViewSet,
    AdminLevel1ViewSet,
    AdminLevel2ViewSet,
    AdminLevel3ViewSet,
    AdminLevel4ViewSet,
    AdminLevel5ViewSet,
)

router = SimpleRouter(trailing_slash=False)
router.register(
    r"world/v1/admin-levels/0", AdminLevel0ViewSet, basename="v1-adminlevel0"
)
router.register(
    r"world/v1/admin-levels/1", AdminLevel1ViewSet, basename="v1-adminlevel1"
)
router.register(
    r"world/v1/admin-levels/2", AdminLevel2ViewSet, basename="v1-adminlevel2"
)
router.register(
    r"world/v1/admin-levels/3", AdminLevel3ViewSet, basename="v1-adminlevel3"
)
router.register(
    r"world/v1/admin-levels/4", AdminLevel4ViewSet, basename="v1-adminlevel4"
)
router.register(
    r"world/v1/admin-levels/5", AdminLevel5ViewSet, basename="v1-adminlevel5"
)

urlpatterns = [
    path("", include(router.urls)),
]