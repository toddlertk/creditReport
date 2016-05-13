from django.db import models
from django.contrib import admin

# Create your models here.
class credit_report(models.Model):
    reportId = models.CharField(max_length=30)
    custId = models.CharField(max_length=18)
    custName = models.CharField(max_length=50)
    queryTime = models.DateTimeField()
    
class credit_report_admin(admin.ModelAdmin):
    list_display = ('reportId', 'custId', 'custName', 'queryTime')

admin.site.register(credit_report, credit_report_admin)