from django.conf.urls import url
from django.contrib import admin
from ..mysite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output, name="script"),
]