from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.index', name='index'),
    # url(r'^$', 'djproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)