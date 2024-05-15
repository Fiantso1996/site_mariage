from django.shortcuts import render

def mariage(request):
    return render(request, 'mariage/index.html')
