from django.conf.urls import url, include
from monitoreo.views import monitoreo_almacenamiento, monitoreo_archivos, monitoreo_auth, monitoreo_procesos, monitoreo_red, monitoreo_usuarios, monitoreo_apache

urlpatterns = [
    #url(r'^$', index),
    url(r'^almacenamiento/$', monitoreo_almacenamiento),
    url(r'^archivos/$', monitoreo_archivos),
    url(r'^auth/$', monitoreo_auth),
    url(r'^procesos/$', monitoreo_procesos),
    url(r'^red/$', monitoreo_red),
    url(r'^usuarios/$', monitoreo_usuarios),
 	url(r'^apache/$', monitoreo_apache),       
]
