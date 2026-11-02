from django.db import models

class Jobs(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending',
        PROCESSING = 'PROCESSING', 'Processing',
        COMPLETED = 'COMPLETED', 'Completed',
        FAILED = 'FAILED', 'Failed'




    id = models.BigAutoField(unique=True)
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    attempts = models.PositiveIntegerField(default=0)
    max_retries = models.PositiveIntegerField(default=3)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Job{self.id} - {self.status}"

