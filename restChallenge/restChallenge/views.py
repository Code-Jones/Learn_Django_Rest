from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET', 'POST'])
def health_test(request, format=None):
    if request.method == 'GET':
        return Response("Okay", status=200)
    elif request.method == 'POST':
        return Response("Okay", status=200)
