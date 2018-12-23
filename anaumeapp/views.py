from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def top(request):
    return render(request, 'templates/top.html', {})

    