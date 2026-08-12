from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
 
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            return redirect("project_list") # Redirect to home or project list
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
