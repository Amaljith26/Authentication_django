from celery import shared_task
from datetime import datetime
import os
from django.conf import settings
from datetime import datetime
from .models import TaskLog

@shared_task
def log_to_file():
    now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_line = f"{now} - log_to_file task executed\n"

    # Ensures consistent location: BASE_DIR/task_log.txt
    log_file_path = os.path.join(settings.BASE_DIR, 'task_log.txt')
    TaskLog.objects.create(message=log_line)

    with open(log_file_path, 'a') as f:
        f.write(log_line)

    return f"Logged at {now}"
