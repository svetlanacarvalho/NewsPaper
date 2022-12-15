from django import template


register = template.Library()

@register.filter()
def censor(value):
    words = ['loser', 'fallen', 'duffer']
    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")
    for i in value.split():
        if i.lower() in words:
            value = value.replace(i, f'{i[0]}{"*" * (len(i)-1)}')
    return value

