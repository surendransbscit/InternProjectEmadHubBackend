from django_q.tasks import schedule
from django.utils import timezone
from django.core.mail import send_mail
from .models import Employee, Taskassigning


def send_daily_task_emails():
    today = timezone.now().date()

    for emp in Employee.objects.all():
        latest_task = Taskassigning.objects.filter(
            employee=emp,
            assigned_at__date=today
        ).order_by('-assigned_at').first()

        if latest_task:
            message = f"Hello {emp.full_name},\n\nYour task for today is: {latest_task.title}\n\nGood luck!"
        else:
            message = f"Hello {emp.full_name},\n\nYou don't have any tasks assigned for today."

        print(f"Sending email to {emp.email}:\n{message}\n")

        send_mail(
            subject=f"Today's Task - {today}",
            message=message,
            from_email='dhileep2005.g@gmail.com',
            recipient_list=[emp.email],
            fail_silently=True,
        )


def schedule_task():
    schedule(
        'intern.tasks.send_daily_task_emails',
        schedule_type='M',
        minutes=3,
        repeats=12
    )


