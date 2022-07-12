from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from core.models import Mail


class MailFormView (LoginRequiredMixin, CreateView):
    login_url = '/admin/'
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

