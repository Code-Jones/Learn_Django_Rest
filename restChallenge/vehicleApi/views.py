import time

from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import status, mixins, generics, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Vehicle_Serializer, History_Serializer
from .models import Vehicle, History
import json


class All_Vehicles(APIView):
    """
    List all vehicles
    """
    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = Vehicle_Serializer(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False)

class Vehicle_Detail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    Basic CRUD Functions based off vehicle private key
    """
    queryset = Vehicle.objects.all()
    serializer_class = Vehicle_Serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Mileage_Details(viewsets.ModelViewSet):
    """
    Update and Get mileage details based off vehicle private key
    """

    serializer_class = History_Serializer
    queryset = History.objects.all()
    lookup_field = "pk"

    def get_Vehicle(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Http404

    """
    Show vehicle mileage history
    """
    @action(detail=True, methods=["GET"])
    def get(self, response, pk):
        history = History.objects.filter(pk)
        serialized = History_Serializer(history, many=True)
        if serialized.is_valid():
            return Response(serialized.data, status=200)
        else:
            return Response("None found")

    """
    Update vehicle mileage by adding history object
    """
    @action(detail=True, methods=["PUT"])
    def put(self, request, pk):
        vehicle = self.get_Vehicle(pk)
        if vehicle.status == Vehicle.Vehicle_Status.INACTIVE or vehicle.status == Vehicle.Vehicle_Status.INOPERATIVE:
            return Response("Cannot Update Inactive Vehicle")
        serialized = History_Serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized.errors, status=400)



@csrf_exempt
def Mileage_Counter(request, pk):
    if request.method == 'GET':
        return HttpResponse(content="send me a date in post")
    elif request.method == 'POST':
        data = json.loads(request.body)
        stripDate = time.strptime(str(data['date']), "%Y-%m-%d")
        history = History.objects.filter(vehicle=pk)
        vehicle = Vehicle.objects.get(pk=pk)
        currentMileage = vehicle.mileage
        if history is None:
            return Http404("No history found for this vehicle")

        for h in history:
            stpd = time.strptime(str(h.date), "%Y-%m-%d")
            if stpd == stripDate:
                return HttpResponse(content=h.milageFromCurrentDate(currentMileage))

        return HttpResponse(content=0)
    else:
        return HttpResponse(content="what are you")

