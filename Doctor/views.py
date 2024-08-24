from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Designation,Specilization,AvailableTime,Review
from .serializer import DoctorSerializer,DesignationSerializer,SpecilizationSerializer,AvailableTimeSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, pagination
# Create your views here.


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class=DoctorPagination
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get("id")
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    

    
    
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
class SpecilizationViewset(viewsets.ModelViewSet):
    queryset = Specilization.objects.all()
    serializer_class = SpecilizationSerializer
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer