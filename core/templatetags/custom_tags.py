from django import template
register = template.Library()
@register.simple_tag
def difficulty_badge_class(level):
    mapping = {
        "Beginner": "bg-success",
        "Intermediate": "bg-warning text-dark",
        "Advanced": "bg-danger",
    }
    return mapping.get(level, "bg-secondary")