from celery import shared_task
from datetime import timedelta
from email.mime.text import MIMEText
from datetime import datetime
from django.utils import timezone
from .models import VisitHistory

@shared_task
def cleanup_old_visits():
    cutoff_date = timezone.now() - timedelta(days=2)
    deleted, _ = VisitHistory.objects.filter(visited_at__lt=cutoff_date).delete()
    print(f"Удалено {deleted} старых записей посещений.")


@shared_task
def send_login_notification(to_email, username, ip_address=None):
    """Отправляет уведомление пользователю об авторизации"""
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = "Уведомление о входе в аккаунт"
    
    text = f"""
    Здравствуйте, {username}!

    Мы зафиксировали вход в ваш аккаунт {time}.
    {f"IP-адрес: {ip_address}" if ip_address else ""}

    Если это были вы — ничего делать не нужно.
    Если нет — срочно измените пароль!
    """

    msg = MIMEText(text)
    msg["Subject"] = subject
    msg["From"] = "noreply@myapp.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("noreply@myapp.com", "YOUR_PASSWORD")
        server.send_message(msg)

    print(f"Письмо об авторизации отправлено пользователю {username}")