from django.shortcuts import render, redirect
from .models import PeopleData
from django.contrib import messages


def home(request):
    return render(request, 'crudoperation/home.html')

def alldata(request):
    if request.method == "POST":
        request_data = request.POST
        first_name = request_data.get('firstname')
        last_name = request_data.get('lastname')
        city = request_data.get('city')
        error_message = None
        if not first_name:
            error_message = 'first name should not empty'
        elif not last_name:
            error_message = 'last name should not empty'
        elif not city:
            error_message = 'city should not empty'
        if not error_message:
            PeopleData(first_name=first_name, last_name=last_name, city=city).save()
            messages.success(request, 'Profile details added')
            return render(request, 'crudoperation/alldata.html')

        else:
            return render(request, 'crudoperation/alldata.html', {'error_message':error_message})
    return render(request, 'crudoperation/alldata.html')
    #     # return redirect('/alldata/')

    # alldata = PeopleData.objects.all()
    # return render(request, 'crudoperation/alldata.html',{'alldata':alldata})
def retrievedata(request):
    alldata = PeopleData.objects.all()
    if alldata:
        return render(request, 'crudoperation/retrievedata.html', {'alldata':alldata})
    else:
        return render(request, 'crudoperation/empty.html')

def deletedata(request, id):
    user = PeopleData.objects.get(pk=id)
    user.delete()
    # alldata = PeopleData.objects.all()
    return redirect('/crudoperation/retrievedata/')
    

def updatedata(request,id):
    if request.method =="POST":
        request_data = request.POST
        first_name = request_data.get('firstname')
        last_name = request_data.get('lastname')
        city = request_data.get('city')
        error_message = None
        if not first_name:
            error_message = 'first name should not empty'
        elif not last_name:
            error_message = 'last name should not empty'
        elif not city:
            error_message = 'city should not empty'
        if not error_message:            
            user_data = PeopleData.objects.get(pk=id)
            user_data.first_name = first_name
            user_data.last_name = last_name
            user_data.city = city
            user_data.save()
            messages.success(request, 'Profile details updated')
            return render(request, 'crudoperation/updatedata.html', {'user_data':user_data})
        else:
            user_data = PeopleData.objects.get(pk=id)
            return render(request, 'crudoperation/updatedata.html', {'error_message':error_message, 'user_data':user_data})

    user_data = PeopleData.objects.get(pk=id)
    return render(request, 'crudoperation/updatedata.html', {'user_data':user_data})

