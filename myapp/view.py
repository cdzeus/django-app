# dans views.py
from django.shortcuts import render

def ma_page(request):
    return render(request, 'ma_page.html')
