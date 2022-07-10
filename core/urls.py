from django.urls import path
from core.views import DeliverView, MailFormView

urlpatterns = [
    path('form/', MailFormView.as_view(), name='form'),
    path('deliver/<slug:uuid>.png', DeliverView.as_view(), name='deliver')
]
