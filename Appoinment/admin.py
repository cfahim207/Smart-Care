from django.contrib import admin
from .models import Appoinment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AppoinmentAdmin(admin.ModelAdmin):
    list_display=['doctor_name','patient_name','appoinment_type','appoinment_status','symptom','time']
    
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appoinment_status== "Running" and obj.appoinment_type=="Online":
            
            email_subject="Your Online Appoinment is Running"
            email_body=render_to_string("admin_email.html",{'user':obj.patient.user, 'doctor':obj.doctor})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
    
admin.site.register(Appoinment,AppoinmentAdmin)