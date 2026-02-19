from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    
    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # User Management (Main Admin Only)
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_sub_admin, name='create_sub_admin'),
    path('users/edit/<int:pk>/', views.edit_sub_admin, name='edit_sub_admin'),
    path('users/toggle-status/<int:pk>/', views.toggle_user_status, name='toggle_user_status'),
]
