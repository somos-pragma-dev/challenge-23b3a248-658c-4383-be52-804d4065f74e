from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from.models import Product

def admin_required(user):
    return user.is_superuser

@login_required
@user_passes_test(admin_required)
def admin_panel(request):
    products = Product.objects.all()
    return render(request, 'admin_panel.html', {'products': products})