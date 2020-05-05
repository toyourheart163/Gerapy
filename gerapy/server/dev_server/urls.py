"""server URL Configuration
"""
import sys

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from .routers import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^docs', include_docs_urls(title='GerapyHub')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# start scheduler
if 'runserver' in sys.argv or 'gunvicorn' in sys.argv or 'heroku' in sys.argv:
    from core.scheduler import sm
    sm.start()
