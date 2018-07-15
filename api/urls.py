from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Our API docs')

urlpatterns = [
    url(r'^doc/$', schema_view),
    url(r'^pit/', include('pit.urls')),
    url(r'^area/', include('area.urls')),
    url(r'^userdata/', include('userdata.urls')),
    url(r'^complaint/', include('complaint.urls')),
]
