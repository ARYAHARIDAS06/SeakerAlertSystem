import psutil
from datetime import datetime

def get_system_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_used_gb": psutil.virtual_memory().used / (1024 ** 3),
        "disk_used_gb": psutil.disk_usage('/').used / (1024 ** 3),
        "uptime_hours": (datetime.now() - datetime.fromtimestamp(psutil.boot_time())).total_seconds() / 3600,
        #"temperature": psutil.sensors_temperatures().get('cpu-thermal', [{}])[0].get('current', 'N/A')
    }
def check_thresholds(metrics):
    alerts = []
    if metrics['cpu_percent'] > 80:
        alerts.append("High CPU usage!")
    if metrics['ram_used_gb'] > 4:  # Example threshold
        alerts.append("High RAM usage!")
    return alerts


# monitor/utils.py

# from django.core.mail import send_mail
# from django.conf import settings
#
# def send_email_notification(subject, message, recipient_list):
#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         recipient_list,
#         fail_silently=False,
#     )
