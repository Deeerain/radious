from django import template

from radio.models import Radio


register = template.Library()


@register.inclusion_tag('radio/newest_radio_list.html')
def draw_newest_radio(count=4):
    queryset = Radio.objects.filter(visible=True).order_by('created')[:count]

    return {
        'object_list': queryset
    }
