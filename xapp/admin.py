
from django.contrib import admin
from xapp.models import patientdetails

class PatientAdmin(admin.ModelAdmin):
    list =['Date','Name','Age','Gender','Address','Contactno','History','Pain','Duration']
admin.site.register(patientdetails,PatientAdmin)