from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an accounts now!
        # Check if passwords match
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Check if username is taken
                user =  User.objects.get(username=request.POST['username'])
                # Route back to signup page with error message
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
                # If username is unique or doesn't exist
            except User.DoesNotExist:
                # Create a new user object
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # After successfully creating a new user object, login
                auth.login(request, user)
                # Return the user to the homepage
                return redirect('home')
        # If passwords didn't match
        else:
            # Route back to signup page with error message
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info!
        return render(request, 'accounts/signup.html')

def login(request):
    # If request is post
    if request.method == 'POST':
        # Check validity of username password combination
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        # If we get a user info back
        if user is not None:
            # Login user
            auth.login(request, user)
            # Return the user to homepage
            return redirect('home')
        # If no user is found
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password is incorrect.'})
    # If request is get
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
