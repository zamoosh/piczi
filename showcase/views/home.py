from .imports import *


def home(request):
    return render(request, 'showcase/index.html')
