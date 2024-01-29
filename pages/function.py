from django import template

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)
