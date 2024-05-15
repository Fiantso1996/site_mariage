from django.shortcuts import render

def maison(request):
    return render(request, 'maison/index.html')