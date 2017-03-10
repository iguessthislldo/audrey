from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Task

@ensure_csrf_cookie
def index(request):
    rv = {'status': 'NO POST'}
    if request.method == 'POST':
        post = request.POST
        if 'request' in post:
            rv = {'status' : 'valid', 'query': [i.name for i in Task.objects.all()]}
        else:
            rv = {"status": "Invalid"}

    return JsonResponse(rv, safe=True)
