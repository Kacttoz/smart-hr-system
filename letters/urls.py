from django.urls import path
from . import views

app_name = 'letters'

urlpatterns = [
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/sub-admin/', views.sub_admin_dashboard, name='sub_admin_dashboard'),
    path('generate/', views.generate_letter, name='generate_letter'),
    path('download/<int:pk>/', views.download_doc, name='download_doc'),
]
