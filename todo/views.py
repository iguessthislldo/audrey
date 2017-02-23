from django.http import JsonResponse

def index(request):
    value = None
    if request.method == 'POST':
        value = request.POST
    else:
        value = "NO POST"

    return JsonResponse(value, safe=False)
