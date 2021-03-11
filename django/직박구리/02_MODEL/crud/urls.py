from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # DOMAIN/crud/....
    path('practice/', include('orm_practice.urls')),
]
