from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MDM.urls')),
    path('scm/', include('SCM.urls')),
    path('', include('WMS.urls')),
]
