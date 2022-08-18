from django.urls import path
from core.views import DeliverView, MailFormView, IndexView, StatusView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('form', MailFormView.as_view(), name='form'),
    path('status', StatusView.as_view(), name='status'),
    path('deliver/<slug:uuid>.png', DeliverView.as_view(), name='deliver')
]
