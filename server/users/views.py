from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated!' )
            return redirect('profile')
    
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)
    contex = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', contex )

def customer_menu(request):
    return render(request, 'users/customer_menu.html')

def customer_home(request):
    return render(request, 'users/customer_home.html')

def customer_order_review(request):
    return render(request, 'users/customer_order_review.html')


def staff(request):
    staffs = User.objects.all()
    
    context = {
        'staffs': staffs
    }
    
    return render(request, 'users/staff.html', context=context)
    