from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/notifs/(?P<user_id>[\d]+)/$', consumers.NotifConsumer),
]
