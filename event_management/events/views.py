# events/views.py
from django.shortcuts import render, redirect
from .models import Events
from django.contrib.auth import authenticate, login#--------for user-admin
from .forms import UserLoginForm, AdminLoginForm#--------for user-admin
from .models import User, AdminUser#--------for user-admin

def index(request):
    return render(request, 'events/index.html')

def events(request):
    data = Events.objects.all()
    return render(request, 'events/events.html', {'data': data})

def contact(request):
    return render(request, 'events/contact.html')

def about(request):
    return render(request, 'events/about.html')

def user_login(request):#--------for user-admin
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'registration/user_login.html', {'form': form})

def admin_login(request):#--------for user-admin
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'registration/admin_login.html', {'form': form})

def admin_dashboard(request):#--------for user-admin
    if request.user.is_authenticated:
        # Check if the user is an admin and render the admin dashboard
        if request.user.is_superuser:
            return render(request, 'registration/admin_dashboard.html')
        else:
            return redirect('user_dashboard')
    else:
        return redirect('registration/admin_login')

def user_dashboard(request):#--------for user-admin
    if request.user.is_authenticated and not request.user.is_superuser:
        return render(request, 'registration/user_dashboard.html')
    else:
        return redirect('registration/user_login')

def set_user_credentials(request):#--------for user-admin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
    return render(request, 'registration/set_user_credentials.html')

def logout(request):
    return render(request, 'registration/logout.html')
