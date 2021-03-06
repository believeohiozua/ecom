from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),    
    path('accounts/', include('allauth.urls')),
    path('account/', include('allauth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


