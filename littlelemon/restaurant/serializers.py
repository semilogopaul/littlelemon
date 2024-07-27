from rest_framework import serializers
from .models import Booking, Menu

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'