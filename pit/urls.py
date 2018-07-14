from rest_framework.routers import DefaultRouter
from pit.views import PitViews


router = DefaultRouter()
router.register(r'pit', PitViews, base_name='Pit')

urlpatterns = router.urls
