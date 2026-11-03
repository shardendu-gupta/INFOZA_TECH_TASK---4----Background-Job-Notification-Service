
from django.core.mail import send_mail


def send_job_email(job):

    result = send_mail(
        subject=job.subject,
        message=job.message,
        from_email=None,
        recipient_list=[job.recipient_email],
        fail_silently=False
    )

    return result
