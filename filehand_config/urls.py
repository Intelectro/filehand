'''
app: filehandarticles_mgr
'''

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns # added as per http://stackoverflow.com/questions/16971794/django-set-the-language
from django.conf.urls.static import static
from django.contrib import admin
from filehand.views import landing
#from . import views # so you can reference views not as strings but directly. see how this helps in debugging when error in view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', landing, name='landing'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^filehand/', include('filehand.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')), # python-social-auth
    url('', include('django.contrib.auth.urls', namespace='auth')),
]   

if settings.DEBUG: # not for production
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)