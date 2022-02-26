from rest_framework import serializers
from .models import Vehicle, History

class History_Serializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ('vehicle', 'date', 'mileage')


class Vehicle_Serializer(serializers.ModelSerializer):
    history = History_Serializer(many=True)

    class Meta:
        model = Vehicle
        fields = ('unit_num', 'mileage', 'manufacturer', 'status', 'history')

    def get_history_set(self, instance):
        history = instance.history_set.all().order_by('-date')
        return History_Serializer(history, many=True).data

    def create(self, validated_data):
        history = validated_data.pop('history')
        vehicle = Vehicle.objects.create(**validated_data)
        for h in history:
            History.objects.create(**h, vehicle=vehicle)
        return vehicle


