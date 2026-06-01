from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


# REGISTER VIEW
def register(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:

        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


# LOGIN VIEW
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            return render(request,
                          'accounts/login.html',
                          {
                              'error':
                              'Invalid Username or Password'
                          })

    return render(request, 'accounts/login.html')


# LOGOUT VIEW
def user_logout(request):

    logout(request)

    return redirect('login')


# MAIN DASHBOARD
@login_required
def dashboard(request):

    if request.user.role == 'student':
        return redirect('student_dashboard')

    elif request.user.role == 'teacher':
        return redirect('teacher_dashboard')

    return redirect('login')


# TEACHER DASHBOARD
@login_required
def teacher_dashboard(request):

    return render(request,
                  'accounts/teacher_dashboard.html')