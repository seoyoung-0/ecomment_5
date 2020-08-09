from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')