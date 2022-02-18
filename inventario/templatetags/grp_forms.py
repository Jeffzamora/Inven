from django import template


register = template.Library()


@register.filter('as_field')
def as_field(form, field):
    return form


@register.filter('as_label')
def as_label(form, field):
    return form[field].label
