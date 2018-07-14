from django.conf.urls import url
from userdata.views import (SendRegistrationUserCodeView, CodeVerificationView)


urlpatterns = [
    url(r'^send_code/$', SendRegistrationUserCodeView.as_view({
        'post': 'create'}), name='send_code'),
    url(r'^code_verification/$', CodeVerificationView.as_view({
        'post': 'create'}),name='code_verification'),
]
