from django.shortcuts import render

# Create your views here.

def MDB4(request):
    return render(request,'MDB4.html')

def spinner(request):
    return render(request,'spinner.html')

def scrollspy(request):
    return render(request,'scrollspy.html')