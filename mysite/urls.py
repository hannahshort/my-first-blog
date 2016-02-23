
from django.conf.urls import url
from django.contrib import admin
#Maybe need to add this!
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
