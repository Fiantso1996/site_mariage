from django.shortcuts import render

def nouvelle(request):
    return render(request, 'nouvelle/index.html')