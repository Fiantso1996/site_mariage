from django.shortcuts import render

def apropos(request):
    return render(request, 'apropos/index.html')
