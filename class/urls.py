from django.contrib import admin
from django.urls import path
from core.views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about)
]
