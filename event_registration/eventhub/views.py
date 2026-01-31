from django.shortcuts import render, redirect

# Home page
def home(request):
    return render(request, 'home.html')