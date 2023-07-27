from django import template

register = template.Library()

def strip_unwanted_characters(value):
    return value.strip("('""',)")

register.filter('strip_unwanted_characters', strip_unwanted_characters)