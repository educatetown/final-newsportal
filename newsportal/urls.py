"""newsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('newsportalapp.urls')),
    path('business/', include('business.urls')),
    path('lifestyle/', include('lifestyle.urls')),
    path('sports/', include('sports.urls')),
    path('covid/', include('covid.urls')),
    path('entertainment/', include('entertainment.urls')),
    path('news/', include('news.urls')),
    path('tech/', include('tech.urls')),
    path('trending/', include('trending.urls')),

    path('advertising/', include('advertise.urls'), name='advertising'),

    path('s/', views.search, name='search'),
        path('team/', views.Team.as_view(), name='team'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

