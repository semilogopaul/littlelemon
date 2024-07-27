from django.shortcuts import render
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]      