from django.shortcuts import render
from django.http import HttpResponse
from _overlapped import NULL
from creditReport.models import credit_report
from encodings import undefined
# Create your views here.

def test_report(request , reportId):
    resu = ""
    try:
        credit = credit_report.objects.get(reportId=reportId)
        resu = "{reportId:" + str(credit.reportId) + ",custId:" + str(credit.custId) \
        + ",custName:" + str(credit.custName) + ",queryTime:" + str(credit.queryTime) + "}"
    except Exception as e:
        print('Error:', e)
    if resu == "":
        resu = " it is error "
    
    return HttpResponse(resu);
