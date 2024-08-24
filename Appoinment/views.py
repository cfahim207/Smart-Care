from django.shortcuts import render
from rest_framework import viewsets
from .models import Appoinment
from .serializer import AppoinmentSerializer
# Create your views here.
class AppoinmentViewset(viewsets.ModelViewSet):
    queryset = Appoinment.objects.all()
    serializer_class = AppoinmentSerializer
    
    
    def get_queryset(self):
        queryset=super().get_queryset()
        patient_id=self.request.query_params.get("patient_id")
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset
    