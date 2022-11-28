from django.shortcuts import render


def allhome(request):
    return render(request, 'allhome.html')
