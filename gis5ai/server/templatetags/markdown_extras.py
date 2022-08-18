#
# This piece of code comes from:
# https://www.webforefront.com/django/jinjacustomfiltersandtests.html
#

from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])
