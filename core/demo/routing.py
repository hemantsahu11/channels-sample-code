from django.template.defaulttags import url
from django.urls import path, re_path
from . import consumers

ws_patterns = [
    path('ws/', consumers.MySyncConsumer.as_asgi()),
]