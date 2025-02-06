# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import NewsletterRequest

from .models import Newsletter

@receiver(post_save, sender=NewsletterRequest)
def send_newsletter(sender, instance, created, **kwargs):
    if created:
        latest_newsletter = Newsletter.objects.latest('created_on')
        subject = latest_newsletter.subject
        pdf_path = latest_newsletter.pdf_file.path

        # Create the email
        email = EmailMessage(
            subject,
            f"Hello {instance.name},\n\nPlease find attached your requested newsletter.",
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
        )

        # Attach the PDF
        with open(pdf_path, 'rb') as pdf_file:
            email.attach('newsletter.pdf', pdf_file.read(), 'application/pdf')
        email.send()
