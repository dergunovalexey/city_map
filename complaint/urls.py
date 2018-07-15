from rest_framework.routers import DefaultRouter
from complaint.views import ComplaintViews


router = DefaultRouter()
router.register(r'complaint', ComplaintViews, base_name='complaint_views')

urlpatterns = router.urls
