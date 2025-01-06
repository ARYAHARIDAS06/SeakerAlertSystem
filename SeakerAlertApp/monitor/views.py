from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import SystemMetrics

def dashboard(request):
    metrics = SystemMetrics.objects.order_by('-timestamp')[:10]
    return render(request, 'dashboard.html', {'metrics': metrics})
