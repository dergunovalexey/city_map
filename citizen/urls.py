from rest_framework.routers import DefaultRouter
from citizen.views import CitizenViews


router = DefaultRouter()
router.register(r'citizen', CitizenViews, base_name='citizen')

urlpatterns = router.urls
