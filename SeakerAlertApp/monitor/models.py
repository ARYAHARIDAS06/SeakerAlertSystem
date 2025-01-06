from django.db import models

# Create your models here.
from django.db import models

class SystemMetrics(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_percent = models.FloatField()
    ram_used_gb = models.FloatField()
    disk_used_gb = models.FloatField()
    uptime_hours = models.FloatField()
    temperature = models.FloatField(null=True, blank=True)
