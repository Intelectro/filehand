'''
    
    Context processors

    use in templates
    
        Locale = {{ LOCALE }}
    
        Equis = {{ EQUIS }}
    
'''
from django.utils.translation import to_locale, get_language

def locale(request):
    return {'LOCALE': to_locale(get_language()) }

def equis(request):
    return {'EQUIS': to_locale(get_language()) }

    