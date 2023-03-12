from django.urls import path
from aicore.views import speech2Text, Text2Image

urlpatterns = [
    # path("", Home.as_view(), name="home"),
    path("", speech2Text, name="speech"),
    path("image/", Text2Image.as_view(), name="image"),
]
