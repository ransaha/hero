from django.conf.urls import url
from django.contrib import admin
from hello import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admission$', views.admission, name='admission'),
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^it$', views.it, name='it'),
    url(r'^math$', views.math, name='math'),
    url(r'^bank$', views.bank, name='bank'),
    url(r'^new$', views.new, name='new'),
    url(r'^success$', views.success, name='success'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^db', views.db, name='db'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

