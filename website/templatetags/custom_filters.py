from django import template
import re

register = template.Library()

@register.filter
def first_sentence(value):
    """Returns the first sentence of the string, including the ending punctuation."""
    if not isinstance(value, str):
        return value
    # Use a regular expression to find the first occurrence of a period or exclamation mark
    match = re.search(r'[.!]', value)
    if match:
        end_pos = match.end()
        return value[:end_pos]
    return value
