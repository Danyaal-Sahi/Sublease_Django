from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('browse')  # Redirect to the homepage or another page
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
