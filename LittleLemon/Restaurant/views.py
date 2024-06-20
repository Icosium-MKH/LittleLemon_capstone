from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView 
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import booking,menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

"""
class bookingitemview(ListCreateAPIView):

    def get(self,request):
        items = booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    

    def post(self,request):
        serializer = bookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":"serializer.data"})
"""        

class MenuItemView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

        

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer


class BookingViewSet(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer


@permission_classes([IsAuthenticated])
@api_view()
#@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})