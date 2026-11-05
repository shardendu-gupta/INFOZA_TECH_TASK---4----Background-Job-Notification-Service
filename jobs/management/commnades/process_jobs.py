import time
from django.core.management.base import BaseCommand
from django.utils import timezone
from jobs.models import Jobs
from jobs.service import send_job_email


class Commnad(BaseCommand):
    help = "Process pending background jobs"

    def add_arguments(self, parser):
        parser.add_argument('--interval', type=int, default=5)
        parser.add_argument('--once', action='store_true')

        def handle(self, *args, **options):
            interval = options['interval']
            once = options['once']

            self.stdout.write(self.style.SUCCESS("Background worked started..."))

            while True:
                job = Jobs.objects.filter(status=Jobs.status.PENDING).order_by('created_at').first()

                if job:

                    try:

                        job.status = Jobs.Status.PROCESSING
                        job.attempts += 1
                        job.error_message = None
                        job.save()

                        self.stdout.write(f"Processing Job {job.id}")
                        

                        send_job_email(job)

                        job.status = Jobs.Status.COMPLETED
                        job.completed_at = timezone.now()
                        job.error_message = None
                        job.save()

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Job {job.id} completed successfully"
                            )
                        )

                    except Exception as e:

                        job.error_message = str(e)

                        if job.attempts < job.max_retries:

                            job.status = Jobs.Status.PENDING

                            self.stdout.write(
                                self.style.WARNING(
                                    f"Job {job.id} failed. Retrying..."
                                )
                            )

                        else:

                            job.status = Jobs.Status.FAILED

                            self.stdout.write(
                                self.style.ERROR(
                                    f"Job {job.id} permanently failed"
                                )
                            )

                        job.save()

                else:

                    self.stdout.write("No pending jobs found.")

                if once:
                    break

                time.sleep(interval)

