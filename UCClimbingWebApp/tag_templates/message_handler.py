from django import template
from django.contrib.messages import constants as message_constants

register = template.Library()

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'error'
}

@register.filter
def message_class(level):
    return MESSAGE_TAGS.get(level, '')