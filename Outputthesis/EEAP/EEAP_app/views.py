from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    return render(request, 'html/homepage.html')

def student_dashboard(request):
    return render(request, 'html/student_dashboard.html')

def vehicle_registration(request):
    if request.method == "POST":
        plate_number = request.POST.get('plnum')
        vehicle_model = request.POST.get('vehicle')
        imageF = request.FILES['imageF']
        imageL = request.FILES['imageL']
        imageR = request.FILES['imageR']
        imageB = request.FILES['imageB']
        ORCR = request.FILES['ORCR']

        vehicle = registered_vehicles.objects.create(fname = "Sample", lname = "User", idnumber = "TUPC-19-0000", 
            platenumber = plate_number, vehiclemodel = vehicle_model, imageF = imageF, imageL = imageL, imageR = imageR,
            imageB = imageB, ORCR = ORCR, status = 'PENDING')
        vehicle.save()
        messages.info(request, 'Successful Registration')
    return render(request, 'html/vehicle_registration.html')

def registered_vehicle(request):
    return render(request, 'html/registered_vehicle.html')

def admin_dashboard(request):
    students = student.objects.all()
    context = {'students' : students}
    return render(request, 'html/admin_dashboard.html',context)

def pending_vehicle(request):
    if request.method == "POST":
        action = request.POST.get('action')
        ids = request.POST.get('id')

        
        if action == "ACCEPT":
            vehicle_status_update = registered_vehicles.objects.get(id = ids)    
            vehicle_status_update.status = "ACCEPTED"
            vehicle_status_update.save()
            
        else:
            vehicle_status_delete = registered_vehicles.objects.get(id = ids)
            vehicle_status_delete.delete()


        
    vehicle_image = registered_vehicles.objects.filter(status = "PENDING")
    context = {'vehicle_image' : vehicle_image }
    return render(request, 'html/pending_vehicle.html',context)