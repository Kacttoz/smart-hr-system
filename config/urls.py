from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', RedirectView.as_view(pattern_name='accounts:login', permanent=False), name='index'),
    path('', include('letters.urls')), # Dashboard and Letter generation
]
