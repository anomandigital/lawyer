from django.shortcuts import render, redirect
from .forms import RegistrationForm


def custom_signup(request):
    if request.method == "GET":
        form = RegistrationForm
        return render(request, 'default-theme/registration/signup.html', {'form2': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.set_password(request.POST['password1'])
            custom_user.save()
            return render(request, 'default-theme/registration/login.html', {'new_user': 'new_user'})
        else:
            form = RegistrationForm()
        return render(request, 'default-theme/registration/signup.html', {'form2': form})
