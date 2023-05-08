from django.shortcuts import render

# Create your views here.

def notfound(request):
    return render(request, '404.html', status=404)