from django import template

register = template.Library()

def tin_format(value):
    if len(value) == 13:
        return f'{value[:3]}-{value[3:6]}-{value[6:9]}-{value[9:]}'
    else:
        return value  # Return original value if it doesn't match the phone format criteria
    
register.filter('tin_format', tin_format)

register = template.Library()