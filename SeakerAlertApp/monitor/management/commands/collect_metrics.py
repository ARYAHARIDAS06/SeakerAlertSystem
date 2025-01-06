# # from django.core.management.base import BaseCommand
# # from monitor.models import SystemMetrics
# # from monitor.utils import get_system_metrics
# #
# # class Command(BaseCommand):
# #     help = 'Collect system metrics and store them in the database.'
# #
# #     def handle(self, *args, **kwargs):
# #         metrics = get_system_metrics()
# #         SystemMetrics.objects.create(
# #             cpu_percent=metrics['cpu_percent'],
# #             ram_used_gb=metrics['ram_used_gb'],
# #             disk_used_gb=metrics['disk_used_gb'],
# #             uptime_hours=metrics['uptime_hours'],
# #             #temperature=metrics.get('temperature', None)
# #         )
# #         self.stdout.write(self.style.SUCCESS('Metrics collected and stored successfully.'))
# #
# #
# # # monitor/management/commands/collect_metrics.py
# #
# # from django.core.management.base import BaseCommand
# # from monitor.models import SystemMetrics
# # from monitor.utils import get_system_metrics, send_email_notification
# #
# #
# # class Command(BaseCommand):
# #     help = 'Collect system metrics and store them in the database.'
# #
# #     def handle(self, *args, **kwargs):
# #         metrics = get_system_metrics()
# #
# #         # Define thresholds
# #         cpu_threshold = 80  # Example threshold for CPU usage
# #         disk_threshold = 50  # Example threshold for disk usage (GB)
# #
# #         # Collect and store the metrics
# #         SystemMetrics.objects.create(
# #             cpu_percent=metrics['cpu_percent'],
# #             ram_used_gb=metrics['ram_used_gb'],
# #             disk_used_gb=metrics['disk_used_gb'],
# #             uptime_hours=metrics['uptime_hours'],
# #             temperature=metrics.get('temperature', None)
# #         )
# #
# #         # Check thresholds and send email if exceeded
# #         if metrics['cpu_percent'] > cpu_threshold:
# #             subject = 'Alert: High CPU Usage'
# #             message = f'CPU usage is {metrics["cpu_percent"]}% which exceeds the threshold of {cpu_threshold}%.'
# #             send_email_notification(subject, message, ['recipient@example.com'])
# #
# #         if metrics['disk_used_gb'] > disk_threshold:
# #             subject = 'Alert: High Disk Usage'
# #             message = f'Disk usage is {metrics["disk_used_gb"]} GB which exceeds the threshold of {disk_threshold} GB.'
# #             send_email_notification(subject, message, ['recipient@example.com'])
# #
# #         self.stdout.write(self.style.SUCCESS('Metrics collected, stored, and alerts sent successfully.'))
#
#
# from django.core.management.base import BaseCommand
# from monitor.models import SystemMetrics
# from monitor.utils import get_system_metrics
# from plyer import notification
#
#
# class Command(BaseCommand):
#     help = 'Collect system metrics and store them in the database with on-screen alerts.'
#
#     def handle(self, *args, **kwargs):
#         # Get the system metrics
#         metrics = get_system_metrics()
#
#         # Store metrics in the database
#         SystemMetrics.objects.create(
#             cpu_percent=metrics['cpu_percent'],
#             ram_used_gb=metrics['ram_used_gb'],
#             disk_used_gb=metrics['disk_used_gb'],
#             uptime_hours=metrics['uptime_hours'],
#             temperature=metrics.get('temperature', None)
#         )
#
#         # Check thresholds and trigger alerts
#         self.check_thresholds(metrics)
#
#         self.stdout.write(self.style.SUCCESS('Metrics collected and stored successfully.'))
#
#     def check_thresholds(self, metrics):
#         # Define thresholds
#         cpu_threshold = 80  # Example: Trigger alert if CPU usage > 80%
#         ram_threshold = 2  # Example: Trigger alert if RAM usage > 2 GB
#         disk_threshold = 50  # Example: Trigger alert if disk usage > 50%
#
#         # Check if metrics exceed thresholds and display alerts
#         if metrics['cpu_percent'] > cpu_threshold:
#             self.show_alert('High CPU Usage', f"CPU Usage is {metrics['cpu_percent']}%!")
#
#         if metrics['ram_used_gb'] > ram_threshold:
#             self.show_alert('High RAM Usage', f"RAM Usage is {metrics['ram_used_gb']} GB!")
#
#         if metrics['disk_used_gb'] > disk_threshold:
#             self.show_alert('High Disk Usage', f"Disk Usage is {metrics['disk_used_gb']} GB!")
#
#     def show_alert(self, title, message):
#         # Show on-screen notification
#         notification.notify(
#             title=title,
#             message=message,
#             timeout=10  # Notification stays for 10 seconds
#         )
from win10toast import ToastNotifier
from django.core.management.base import BaseCommand

from monitor.utils import get_system_metrics  # Adjust the path as needed
from monitor.models import SystemMetrics
class Command(BaseCommand):
    help = 'Collect system metrics and store them in the database with on-screen alerts.'

    def handle(self, *args, **kwargs):
        # Get the system metrics
        metrics = get_system_metrics()

        # Store metrics in the database
        SystemMetrics.objects.create(
            cpu_percent=metrics['cpu_percent'],
            ram_used_gb=metrics['ram_used_gb'],
            disk_used_gb=metrics['disk_used_gb'],
            uptime_hours=metrics['uptime_hours'],
            temperature=metrics.get('temperature', None)
        )

        # Check thresholds and trigger alerts
        self.check_thresholds(metrics)

        self.stdout.write(self.style.SUCCESS('Metrics collected and stored successfully.'))

    def check_thresholds(self, metrics):
        # Define thresholds
        cpu_threshold = 80  # Example: Trigger alert if CPU usage > 80%
        ram_threshold = 2  # Example: Trigger alert if RAM usage > 2 GB
        disk_threshold = 50  # Example: Trigger alert if disk usage > 50 GB

        # Create a ToastNotifier object
        toaster = ToastNotifier()

        # Check if metrics exceed thresholds and display alerts
        if metrics['cpu_percent'] > cpu_threshold:
            toaster.show_toast('High CPU Usage', f"CPU Usage is {metrics['cpu_percent']}%", duration=10)

        if metrics['ram_used_gb'] > ram_threshold:
            toaster.show_toast('High RAM Usage', f"RAM Usage is {metrics['ram_used_gb']} GB", duration=10)

        if metrics['disk_used_gb'] > disk_threshold:
            toaster.show_toast('High Disk Usage', f"Disk Usage is {metrics['disk_used_gb']} GB", duration=10)
