from .imports import *


class PictureView(viewsets.ModelViewSet):
    queryset = Picture.objects.all().order_by('name')
    serializer_class = PictureSerializer
