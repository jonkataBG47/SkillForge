from django import template
register = template.Library()
@register.filter
def hours_to_days(hours):
    return round(float(hours) / 8, 1)