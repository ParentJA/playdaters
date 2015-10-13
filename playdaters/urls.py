__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/v1/chats/', include('chats.urls')),
    url(r'^api/v1/children/', include('children.urls')),
    url(r'^api/v1/friends/', include('friends.urls')),
    url(r'^api/v1/play_dates/', include('play_dates.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# Serves static files in development environment...
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serves media files in development environment...
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
