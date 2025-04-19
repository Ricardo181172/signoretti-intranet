# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'home.html', context)  # Vamos criar este template

@login_required(login_url='login')
def crm_view(request):   
    return render(request, 'crm.html')