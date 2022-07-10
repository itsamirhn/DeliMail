import uuid

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone


class Mail(models.Model):

    to = models.EmailField()
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)

    uuid = models.UUIDField(editable=False, default=uuid.uuid4, db_index=True, unique=True)

    sent_at = models.DateTimeField(null=True)
    delivered_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def send(self):
        html_message = render_to_string('core/mail.html', {'mail': self})
        email = EmailMultiAlternatives(
            self.subject,
            self.message,
            settings.EMAIL_FROM,
            [self.to],
            alternatives=[(html_message, 'text/html')]
        )
        email.send()
        self.sent_at = timezone.now()
        self.save()

    def delivered(self):
        self.delivered_at = timezone.now()
        self.save()
