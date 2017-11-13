from django import template

register = template.Library()

@register.filter
def modulus(value, num):
    return value % num
