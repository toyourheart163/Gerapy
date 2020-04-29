"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from .routers import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gerapy.server.core.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^docs', include_docs_urls(title='GerapyHub')),
]

if 'runserver' in sys.argv:
    # start scheduler
    from gerapy.server.core.scheduler import sm
    sm.start()
