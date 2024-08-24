from django.db import models
from Patient.models import Patient
from Doctor.models import Doctor,AvailableTime
# Create your models here.

APPOINMENT_TYPE=[
    ('Online','Online'),
    ('Offline','Offline'),
]
APPOINMENT_STATUS=[
    ('Complete','Complete'),
    ('Running','Running'),
    ('Pending','Pending'),
]
class Appoinment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appoinment_type=models.CharField(choices=APPOINMENT_TYPE,max_length=10)
    appoinment_status=models.CharField(choices=APPOINMENT_STATUS,max_length=10,default="Pending")
    symptom=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
    
    