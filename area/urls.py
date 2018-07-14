from rest_framework.routers import DefaultRouter
from area.views import MicroAreaViews


router = DefaultRouter()
router.register(r'micro_area', MicroAreaViews, base_name='micro_area')

urlpatterns = router.urls
