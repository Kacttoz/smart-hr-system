from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import SubAdminCreationForm, SubAdminEditForm # We need to create these forms

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'MAIN_ADMIN' or user.is_superuser:
                return reverse_lazy('letters:admin_dashboard')
            else:
                return reverse_lazy('letters:sub_admin_dashboard')
        return reverse_lazy('letters:sub_admin_dashboard')

@login_required
def user_list(request):
    if not request.user.role == 'MAIN_ADMIN' and not request.user.is_superuser:
        return redirect('letters:sub_admin_dashboard')
        
    sub_admins = User.objects.filter(role='SUB_ADMIN')
    return render(request, 'accounts/user_list.html', {'sub_admins': sub_admins})

@login_required
def create_sub_admin(request):
    if not request.user.role == 'MAIN_ADMIN' and not request.user.is_superuser:
        return redirect('letters:sub_admin_dashboard')
        
    if request.method == 'POST':
        form = SubAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'SUB_ADMIN'
            user.save()
            messages.success(request, f"Sub-Admin {user.username} created successfully.")
            return redirect('accounts:user_list')
    else:
        form = SubAdminCreationForm()
        
    return render(request, 'accounts/user_form.html', {'form': form, 'title': 'Create Sub Admin'})

@login_required
def edit_sub_admin(request, pk):
    if not request.user.role == 'MAIN_ADMIN' and not request.user.is_superuser:
        return redirect('letters:sub_admin_dashboard')
        
    user_obj = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        form = SubAdminEditForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f"Sub-Admin {user_obj.username} updated.")
            return redirect('accounts:user_list')
    else:
        form = SubAdminEditForm(instance=user_obj)
        
    return render(request, 'accounts/user_form.html', {'form': form, 'title': 'Edit Sub Admin'})

@login_required
def toggle_user_status(request, pk):
    if not request.user.role == 'MAIN_ADMIN' and not request.user.is_superuser:
        return redirect('letters:sub_admin_dashboard')
        
    user_obj = get_object_or_404(User, pk=pk)
    if user_obj.is_superuser:
        messages.error(request, "Cannot deactivate superuser.")
        return redirect('accounts:user_list')
        
    user_obj.is_active = not user_obj.is_active
    user_obj.save()
    status = "activated" if user_obj.is_active else "deactivated"
    messages.success(request, f"User {user_obj.username} has been {status}.")
    return redirect('accounts:user_list')
