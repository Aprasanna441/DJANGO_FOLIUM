from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    latitude1=serializers.FloatField()
    longitude1=serializers.FloatField()