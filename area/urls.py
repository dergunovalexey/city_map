from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from area.views import MicroAreaViews, PointsViews


router = DefaultRouter()
router.register(r'micro_area', MicroAreaViews, base_name='micro_area')

urlpatterns = [
    url(r'^get_points/$', PointsViews.as_view({'post': 'create'})),
]

urlpatterns += router.urls
