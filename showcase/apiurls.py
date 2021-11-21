from rest_framework import routers
# from .api import *
from .api.PictureView import PictureView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', PictureView)

urlpatterns = [
    path('', include(router.urls))
]
