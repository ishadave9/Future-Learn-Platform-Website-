from django.shortcuts import render,HttpResponseRedirect,redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def course(request):
    return render(request,'Courses.html')

def course_form(request):
    return render(request,'Course-form.html')

def quiz(request):
    return render(request,'Quiz.html')

def contact(request):
    return render(request,'Contact.html')

# @login_required(login_url='/logout/')
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        email = request.POST.get('email')
        
        if password != password_repeat:
            messages.error(request, 'Passwords do not match')
            return HttpResponseRedirect('/')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return HttpResponseRedirect('/')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return HttpResponseRedirect('/')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Account created successfully')
        return HttpResponseRedirect('/login/')
    else:
        return render(request, 'login_signup.html')




# @login_required(login_url='/logout/')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('/index/')  # Redirect to home page or any desired page
        else:
            # Return with an error message
            return render(request, 'login_signup.html', {'error': 'Invalid username or password'})
    else:
        # Render the login page
        return render(request, 'login_signup.html')
@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')