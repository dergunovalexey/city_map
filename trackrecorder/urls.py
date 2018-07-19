from rest_framework.routers import DefaultRouter
from trackrecorder.views import RoadTrackViews


router = DefaultRouter()
router.register(r'road_track', RoadTrackViews, base_name='road_track')

urlpatterns = router.urls
