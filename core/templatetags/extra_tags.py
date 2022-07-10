from django import template
from django.urls import reverse
from DeliMail.settings import HOST_URL

register = template.Library()


@register.simple_tag(takes_context=True)
def abs_url(context, view_name, *args, **kwargs):
    if 'request' in context:
        return context['request'].build_absolute_uri(reverse(view_name, args=args, kwargs=kwargs))
    return HOST_URL + reverse(view_name, args=args, kwargs=kwargs)
