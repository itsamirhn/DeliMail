from django.urls import path
from core.views import DeliverView, MailFormView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('form/', MailFormView.as_view(), name='form'),
    path('deliver/<slug:uuid>.png', DeliverView.as_view(), name='deliver')
]
