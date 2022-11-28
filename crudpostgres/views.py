from django.shortcuts import render, redirect
from .models import student2
from django.contrib import messages


def home(request):
    return render(request, 'crudpostgres/home.html')


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
            student2(first_name=first_name, last_name=last_name, city=city).save()
            messages.success(request, 'Profile details added')
            return render(request, 'crudpostgres/alldata.html')

        else:
            return render(request, 'crudpostgres/alldata.html', {'error_message':error_message})
    return render(request, 'crudpostgres/alldata.html')
    #     # return redirect('/alldata/')

    # alldata = student2.objects.all()
    # return render(request, 'crudpostgres/alldata.html',{'alldata':alldata})
def retrievedata(request):
    alldata = student2.objects.all()
    if alldata:
        return render(request, 'crudpostgres/retrievedata.html', {'alldata':alldata})
    else:
        return render(request, 'crudpostgres/empty.html')


def deletedata(request, id):
    user = student2.objects.get(pk=id)
    user.delete()
    # alldata = student2.objects.all()
    return redirect('/crudpostgres/retrievedata3/')


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
            user_data = student2.objects.get(pk=id)
            user_data.first_name = first_name
            user_data.last_name = last_name
            user_data.city = city
            user_data.save()
            messages.success(request, 'Profile details updated')
            return render(request, 'crudpostgres/updatedata.html', {'user_data':user_data})
        else:
            user_data = student2.objects.get(pk=id)
            return render(request, 'crudpostgres/updatedata.html', {'error_message':error_message, 'user_data':user_data})

    user_data = student2.objects.get(pk=id)
    return render(request, 'crudpostgres/updatedata.html', {'user_data':user_data})

