import pathlib

from django.urls import reverse_lazy
from core.models import Mail
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views import View
from django.conf import settings


class MailFormView (CreateView):
    model = Mail
    fields = ['to', 'subject', 'message']
    success_url = reverse_lazy('form')

    def form_valid(self, form):
        mail: Mail = form.instance
        mail.send()
        return super().form_valid(form)


class DeliverView (View):

    def get(self, request, uuid, *args, **kwargs):
        mail = get_object_or_404(Mail, uuid=uuid)
        mail.delivered()
        return FileResponse(open('1x1.png', 'rb'))

