from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    print(f"Applying class '{arg}' to field '{value}'")
    return value.as_widget(attrs={'class': arg})
